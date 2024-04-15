from django.urls import path
from . import views

urlpatterns = [
    # 클래스 기반의 뷰(CBV)를 사용할 때는 반드시 as_view() 함수를 호출해야 한다.
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),

]
