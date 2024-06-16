from django.shortcuts import render

from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm

# FormView 클래스
#   사용자의 입력을 받을 수 있는 Form을 form_class으로 지정한다.
#   폼을 구현한 클래스를 지정하여, 원하는 템플릿에 간단하게 표현할 수 있다.
#   사용할 템플릿을 templates_name으로 지정한다.
#      사용할 템플릿과 연결되는 속성 변수를 따로 설정하지 않아도 자동 인식된다.
class RegisterView(FormView):
    template_name='register.html'
    form_class=RegisterForm
    success_url="/"

class LoginView(FormView):
    template_name='login.html'
    form_class=LoginForm
    success_url="/"

    # View에서 세션에 로그인 정보를 저장
    #   LoginForm에서 모든 유효성 검사가 성공적으로 끝났을 때 호출된다.
    #   form 변수에, 유효성 검증에 성공한 form 객체가 들어온다.
    #   super()를 활용하여 부모클래스의 form_valid 함수도 호출한다.
    def form_valid(self, form):
        self.request.session['user'] = form.user_id

        return super().form_valid(form)