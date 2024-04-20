from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

# CustomUser 모델 정의 후 관리자 페이지에 User 모델 수동 등록

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # "fields" 키 값의 튜플이 하나의 요소만 갖는 경우에는 반드시 마지막에 쉼표가 붙어야 한다.
    #   튜플 특성상, 쉼표로 연결되면 괄호가 감싸지지 않아도 class 'tuple'로 출력된다.
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("개인정보", {"fields": ("first_name", "last_name", "email")}),
        ("추가필드", {"fields": ("profile_image", "short_description")}),
        ("권한", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("중요한 일정", {"fields": ("last_login", "date_joined")}),
    )



    