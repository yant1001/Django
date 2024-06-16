# 브라우저에 텍스트를 돌려주고 싶을 경우 HttpResponse 객체를 리턴해줘야함
from django.http import HttpResponse
# 장고에서 HTML 파일을 브라우저에 돌려주기 위해 사용하는 함수
from django.shortcuts import render
from burgers.models import Burger

def main(request):
    # 첫번째 인수: request -> view 함수에 자동으로 전달되는 request 객체를 지정
    # 두번째 인수: 템플릿의 경로 지정 (settings.py에 적힌 TEMPLATE_DIR 기준)
    return render(request, 'main.html')

def burger_list(request):
    burgers = Burger.objects.all()
    
    # print하면 브라우저가 아닌 콘솔창에 출력된다.
    #   View는 Model 클래스를 사용해서 DB로부터 원하는 데이터를 가져오고, 그 데이터를 템플릿으로 전달한다.
    #   Template은 View 함수가 전달해준 데이터를 사용해서 동적으로 HTML을 구성한다.
    print('전체 햄버거 목록:', burgers)

    # Template으로 가져온 데이터를 전달해줄 때는 파이썬의 dict 객체를 사용한다.
    #   관용적으로 Template에 전달되는 사전 객체의 변수명은 context이다.
    context = {
        # burgers 키에 burgers 변수(queryset 객체, 위에서 all로 정의됨)를 전달한다. (왼쪽 burgers 키는 바뀔 수 있다)
        'burgers': burgers,
    }

    # render의 세번째 인수는 Template에 전달해줄 dict 객체
    return render(request, 'burger_list.html', context)

def burger_search(request):
    # request.GET에서 keyword 키의 값을 가져와 출력한다.
    # filter -> 조건과 일치하는 객체를 모두 돌려준다.
    # name__contains=keyword -> name 속성이 keyword 변수의 값을 포함하는 경우
    # name_exact=keyword or name=keyword -> name 속성이 정확이 keyword 변수의 값인 경우
    # 아래는 주소표시줄로 keyword가 주어지지 않다라도 에러가 나지 않도록 하는 코드
    keyword = request.GET.get('keyword')
    if keyword is not None:
        burgers = Burger.objects.filter(name__contains=keyword)
    else:
        burgers = Burger.objects.none()
    context = {
        'burgers': burgers,
    }
    return render(request, 'burger_search.html', context)