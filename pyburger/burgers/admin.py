from django.contrib import admin
from burgers.models import Burger

# 각 app마다 admin.py가 있다.

@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    pass