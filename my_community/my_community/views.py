# from django.http import HttpResponse
from django.shortcuts import render
# from user.models import User
import os

def home(request):
    # 세션에 저장된 user의 id(uid) 가져오기
    # uid = request.session.get('user')

    # uid가 존재한다면
    # if uid:
        # 모델을 이용해 데이터베이스에서 uid를 넣어서 조회
        # user = User.objects.get(pk=uid)
        # return render(request, 'home.html')

    return render(request, 'home.html')

