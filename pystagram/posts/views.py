from django.shortcuts import render, redirect

def feeds(request):
    # View 함수에 전달된 요청(request)에서 사용자 정보는 request.user 속성으로 가져온다.
    #   로그인하지 않은 경우 AnonymousUser 출력
    # 가져온 request.user가 로그인 사용자인지에 대한 여부를 is_authenticated 속성으로 확인
    #   로그인하지 않은 경우 False 출력

    # feed 레이지에 접근하는 사용자가 로그인하지 않은 경우 '/users/login/'으로 이동
    if not request.user.is_authenticated:
        return redirect('/users/login/')
    return render(request, 'posts/feeds.html')