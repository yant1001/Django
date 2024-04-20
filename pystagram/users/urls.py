from django.urls import path
from users.views import login_view

# pyburger, pylog에서는 URLconf(urls.py) 파일을 프로젝트 폴더 안에 하나만 만들어서 사용했다.
#   app별로 urls.py 파일을 따로 만들면 url을 분리할 수 있다.
# app별로 새로운 urls.py 파일을 만들었다면 기본 프로젝트 폴더의 URLconf에 
#   새로 만든 URLconf를 사용하도록 설정을 추가해야 한다. (include 사용)

urlpatterns = [
    # Root URLconf에서 include 함수를 사용해 users의 urls.py 내용을 가져온다.
    # "users/login/" 경로: config/urls.py → users/urls.py → login_view 함수
    path("login/", login_view),
]
