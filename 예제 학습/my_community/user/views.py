from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .forms import LoginForm

# Create your views here.


def register(request):
    # 사용자의 요청이 GET인 경우
    if request.method == 'GET':
        return render(request, 'register.html')
        # 사용자의 요청이 POST인 경우
    elif request.method == 'POST':
        # 각 input tag에서 name 속성값을 이용해 사용자가 보낸 값을 꺼내옵니다.
        user_id = request.POST.get('user_id', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)

        # 가입시 비밀번호 일치 확인을 위해 받아옵니다.
        # 실제로는 frontend에서 담당하지만, 여기서는 backend에서 담당하도록 하겠습니다.
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (user_id and useremail and password and re_password):
            res_data['error'] = "모든 값을 입력해야 합니다."
        elif password != re_password:
            res_data['error'] = "비밀번호가 다릅니다~!"
        else:
            user = User(user_id=user_id, useremail=useremail, password=make_password(password))
            user.save()

        return render(request, 'register.html', res_data)

def login(request):
    if request.method == 'POST':
        # 폼 객체 생성 시에 사용자가 post로 넘긴 모든 데이터를 기본적으로 세팅
        # 사용자가 보낸 내용을 자동으로 form에 세팅합니다.
        form = LoginForm(request.POST)
        
        # 사용자가 입력한 값이 유효하다면
        if form.is_valid():
            # 이제 is_valid()가 True면 form에 user의 pk가 들어 있습니다.
            request.session['user'] = form.user_id
            # 메인 페이지로 이동
            return redirect("/")
    else:
        # GET 방식으로 요청하면 비어있는 form을 생성
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
    

def logout(request):
    # 현재 로그인한 사용자의 정보가 세션에 존재하면
    if request.session.get('user'):
        del(request.session['user']) # user 정보 삭제
    
    # 로그아웃 수행 후 홈 페이지로 이동
    return redirect("/")