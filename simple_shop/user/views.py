from django.shortcuts import render

from django.views.generic.edit import FormView
from .forms import RegisterForm

# FormView 클래스
#   사용자의 입력을 받을 수 있는 Form을 form_class으로 지정한다.
#   폼을 구현한 클래스를 지정하여, 원하는 템플릿에 간단하게 표현할 수 있다.
#   사용할 템플릿을 templates_name으로 지정한다.
#      사용할 템플릿과 연결되는 속성 변수를 따로 설정하지 않아도 자동 인식된다.
class RegisterView(FormView):
    template_name='register.html'
    form_class=RegisterForm

