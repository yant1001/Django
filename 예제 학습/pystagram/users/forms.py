from django import forms
from django.core.exceptions import ValidationError
from users.models import User

# models.py의 Model 클래스가 데이터베이스의 테이블이라면,
# forms.py의 Form 클래스는 HTML의 <form> 태그 안에 들어가는 요소들을 정의한다.
#   forms.py는 기본으로 생성되지 않기 때문에 새로 만들어야 한다.
#   Model 클래스와 Form 클래스는 유사한 형태이다. (Field가 정의됨)

# Template에서 LoginForm을 사용하기 위해서는, 
#   View 함수에서 LoginForm을 생성하고 Template에 전달해야 한다.
class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(attrs={
            'placeholder': '사용자명 (3자리 이상)'
            },),
        )
    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(attrs={
            'placeholder': '비밀번호 (4자리 이상)'
        },),
        )

class SignupForm(forms.Form):
    username = forms.CharField()
    # forms.PasswordInput 위젯은 비밀번호를 별로 변환하는 기능
    password1 = forms.CharField(widget=forms.PasswordInput)
    # 비밀번호 확인 용도
    password2 = forms.CharField(widget=forms.PasswordInput)
    profile_image = forms.ImageField()
    short_description = forms.CharField()

    def clean_username(self):
        username = self.cleand_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"입력한 사용자명({username})은 이미 사용 중입니다.")
        return username
    
    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            self.add_error("password2", "비밀번와 비밀번호 확인란의 값이 다릅니다.")

    def save(self):
        username = self.cleaned_data["username"]
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        profile_image = self.cleaned_data["profile_image"]
        short_description = self.cleaned_data["short_description"]
        
        # Form에 에러가 없을 경우(True값), 곧바로 User를 생성하고 로그인 후 피드 페이지로 이동한다. 
        user = User.objects.create_user(
            username=username,
            password=password1,
            profile_image=profile_image,
            short_description=short_description
        )
        return user