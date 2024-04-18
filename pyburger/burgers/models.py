from django.db import models

# 장고의 Model은 DB의 테이블과 같다.
# Model 역할을 하는 클래스를 만들 때는 반드시 장고의 models.Model 클래스를 상속받아야 한다.
# models.Model 클래슬 상속받아야지만 데이터베이스에서 하나의 테이블 역할을 하게 된다.

# class를 적는 것은 테이블의 형태를 정의한 것일뿐, 실제 테이블을 생성하려면 마이그레이션해야 한다.
class Burger(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)
