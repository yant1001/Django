from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('regist/', views.ProductRegister.as_view()),
    path('detail/<int:pk>/', views.ProductDetail.as_view()),
]