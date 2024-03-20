"""my_community URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home

# 강의교재에는 from user.views import home이었으나 자꾸 오류나서 확인
# my_community 폴더에서 만든 views파일의 home 함수니까 .views로 변경

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),  # user app의 urls.py에 등록된 url 포함시키기
    path('board/', include('board.urls')),
    path('', home),
]
