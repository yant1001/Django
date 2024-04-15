from django.shortcuts import render

# my_community 프로젝트에서는 FBV(함수 기반 View) 방식으로 작성
#   함수로 만들어진 기능은 객체지향 프로그래밍의 상속 기능을 활용하기 어렵다.
# simple_shop 프로젝트에서는 CBV(클래스 기반 View) 방식으로 작성
#   클래스를 이용해 자주 사용하는 요소를 상속 및 커스텀. Generic View라고 한다.
def index(request):
    return render(request, 'index.html')