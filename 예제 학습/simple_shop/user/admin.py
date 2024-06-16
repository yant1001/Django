from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    # 관리자 화면에서 노출할 항목을 작성한다.
    #   이때 항목이 한 개라도 반드시 뒤에 콤마를 붙여야 오류가 발생하지 않는다.
    list_display=('email', )

admin.site.register(User, UserAdmin)