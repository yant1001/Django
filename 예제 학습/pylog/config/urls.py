"""config URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blog.views import post_list, post_detail, post_add
from config.views import index




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('posts/', post_list),
    # <> 사이의 값은 동적으로 값을 받을 수 있는 영역이다.
    #   왼쪽 값인 int는 <> 사이 영역이 정수 형태의 값만 받는다는 의미
    #   오른쪽 값인 post_id는 <> 사이 영역이 post_id라는 이름을 갖는다는 의미
    path('posts/<int:post_id>/', post_detail),
    path('posts/add/', post_add),
]

urlpatterns += static(
    # 어떤 URL 접두어가 올 때 정적파일을 돌려줄 것인지
    prefix=settings.MEDIA_URL,
    # 어디에서 정적파일을 찾아 돌려줄 것인지
    document_root=settings.MEDIA_ROOT,
)