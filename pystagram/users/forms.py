from django import forms

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