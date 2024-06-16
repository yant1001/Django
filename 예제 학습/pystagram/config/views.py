from django.shortcuts import render, redirect

def index(request):
    # 루트 경로에서, 로그인되어 있는 경우 feed 페이지로 redirect
    if request.user.is_authenticated:
        return redirect('/posts/feeds/')
    # 루트 경로에서, 로그인되어 있지 않은 경우 login 페이지로 redirect
    else:
        return redirect('/users/login/')
    return render(request, "index.html")