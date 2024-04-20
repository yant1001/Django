from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import LoginForm, SignupForm

def login_view(request):
    # 로그인 페이지에 접근하는 사용자가 이미 로그인되어 있는 경우
    if request.user.is_authenticated:
        return redirect('/posts/feeds/')
    
    if request.method == 'POST':
        # LoginForm 인스턴스를 생성한다.
        #   users.forms의 LoginForm 클래스를 form이라는 변수에 담은 형태
        form = LoginForm(data=request.POST)

        # LoginForm에 들어온 데이터가 적절한지 유효성 검사
        #   Form 클래스를 사용해 데이터를 받았다면, 반드시 is_valid 호출
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # username, password에 해당하는 사용자가 있는지 검사
            user = authenticate(username=username, password=password)
            # 해당 사용자가 존재한다면 (회원가입된 사용자)
            if user:
                login(request, user)
                return redirect('/posts/feeds/')
            else:
                form.add_error(None, '입력한 자격증명에 해당하는 사용자가 없습니다.')

        # 어떤 경우든 실패했다면, (데이터 검증이나 사용자 검사) 다시 LoginForm을 사용한 로그인 페이지로 렌더링
        #   생성한 LoginForm 인스턴스를 템플릿에 "form"이라는 키로 전달한다.
        context = {"form": form,}

        return render(request, "users/login.html", context)

    else:
        # POST일 경우와 달리, GET 방식일 땐 data 인수를 전달하지 않는다.
        #   data 없이 생성된 Form은 Template에 form 정보를 전달하기 위해 사용된다.
        #   data 인수를 채운 Form은 해당 data의 유효성을 검증하기 위해 사용된다.
        form = LoginForm()
        context = {'form': form}

        return render(request, "users/login.html", context)

def logout_view(request):
    # logout 함수 호출에 request를 전달한다.
    # 장고 기본 규칙에서 로그아웃은 GET, POST 관계없이 동작하지만,
    #   P0ST 요청에서만 동작하게 하고 싶다면 request.method에 따라 동작을 다르게 변형해 사용한다.
    logout(request)
    return redirect('/users/login/')

def signup(request):
    # View에서 Template에 SignupForm을 전달하는 역할
    #   SignupForm 인스턴스를 생성, Template에 전달한다.
    form = SignupForm()
    context = {'form': form}
    return render(request, 'users/signup.html', context)