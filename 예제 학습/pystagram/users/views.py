from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import LoginForm, SignupForm

from users.models import User

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
    return redirect('login/')

def signup(request):
    if request.method == "POST":
        # Form이 문자열과 파일 데이터를 둘 다 가지고 있다면 Form 생성 시 data와 files 모두 전달해야 한다.
        form = SignupForm(data=request.POST, files=request.FILES)
        # is_valid()로 유효성 검증한 값이 True일 때, 입력받은 값들을 변수로 할당하는 단계
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/posts/feeds/")
        # Form에 에러가 있다면, 즉 위의 POST 요청이 유효하지 않다면, 아래의 context~ 부분으로 이동

    # GET 요청에는 빈 Form을 보여준다.
    # View에서 Template에 SignupForm을 전달하는 역할
    #   SignupForm 인스턴스를 생성, Template에 전달한다.
    else:
        form = SignupForm()

    # context로 전달되는 form의 경우의 수
    # 1. POST 요청에서 생성된 form이 유효하지 않은 경우 >> 에러를 포함한 form이 사용자에게 보여진다.
    # 2. GET 요청으로 빈 form이 생성되는 경우 >> 빈 form이 사용자에게 보여진다.
    context = {'form': form}
    return render(request, 'users/signup.html', context)

