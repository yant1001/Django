# 브라우저에 텍스트를 돌려주고 싶을 경우 HttpResponse 객체를 리턴해줘야함
from django.http import HttpResponse
# 장고에서 HTML 파일을 브라우저에 돌려주기 위해 사용하는 함수
from django.shortcuts import render

def main(request):
    # 첫번째 인수: request -> view 함수에 자동으로 전달되는 request 객체를 지정
    # 두번째 인수: 템플릿의 경로 지정 (settings.py에 적힌 TEMPLATE_DIR 기준)
    return render(request, 'main.html')

def burger_list(request):
    return render(request, 'burger_list.html')