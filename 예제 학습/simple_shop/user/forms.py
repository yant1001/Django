from django import forms
from .models import User
from django.contrib.auth.hashers import make_password, check_password

class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={'required': '이메일을 입력해주세요.'},
        max_length=64,
        label='이메일'
    )

    password = forms.CharField(
        error_messages={'required': '비밀번호를 입력해주세요.'},
        widget=forms.PasswordInput,
        label='비밀번호'
    )

    re_password = forms.CharField(
        error_messages={'required': '비밀번호를 입력해주세요.'},
        widget=forms.PasswordInput,
        label='비밀번호 확인'
    )

    # 유효성 검증
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        if password and re_password:
            if password != re_password:
                self.add_error("password", "비밀번호가 서로 다릅니다.")
                self.add_error("re_password", "비밀번호가 서로 다릅니다.")

            else:
                user = User(
                    email = email,
                    password = make_password(password)
                )
                user.save()


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={'required': '이메일을 입력해주세요.'},
        max_length=64,
        label='이메일'
    )

    password = forms.CharField(
        error_messages={'required': '비밀번호를 입력해주세요.'},
        widget=forms.PasswordInput,
        label='비밀번호'
    )

    # 유효성 검증
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                self.add_error("email", "등록되지 않은 이메일 입니다.")
                return
            if not check_password(password, user.password):
                self.add_error("password", "비밀번호를 틀렸습니다.")
            else:
                self.user_id=user.id