from django.shortcuts import render, redirect
from users.forms import LoginForm

def login_view(request):
    # 로그인 페이지에 접근하는 사용자가 이미 로그인되어 있는 경우
    if request.user.is_authenticated:
        return redirect('/posts/feeds/')
    
    # LoginForm 인스턴스를 생성한다.
    #   users.forms의 LoginForm 클래스를 form이라는 변수에 담은 형태
    form = LoginForm()
    # 생성한 LoginForm 인스턴스를 템플릿에 "form"이라는 키로 전달한다.
    context = {
        "form": form,
    }
    return render(request, "users/login.html", context)