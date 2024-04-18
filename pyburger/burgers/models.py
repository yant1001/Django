from django.db import models

# 장고의 Model은 DB의 테이블과 같다.
# Model 역할을 하는 클래스를 만들 때는 반드시 장고의 models.Model 클래스를 상속받아야 한다.
# models.Model 클래슬 상속받아야지만 데이터베이스에서 하나의 테이블 역할을 하게 된다.

# class를 적는 것은 테이블의 형태를 정의한 것일뿐, 실제 테이블을 생성하려면 마이그레이션해야 한다.
# db 테이블의 이름은 기본적으로 appname_classname으로 자동 저장된다. (ex. burgers_burger)
class Burger(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)

    # admin 페이지에서 Burgers 메뉴의 햄버거 객체의 이름을 쉽게 알아볼 수 있도록 클래스에 추가 설명을 작성하는 것
    # 모델 클래스의 인스턴스를 어떻게 표현할지 나타낸다.
    # 아래의 경우 Burger 인스턴스의 name 속성을 나타내는 형태이다.
    def __str__(self):
        # all(), get(), values(), filter() 사용해서 정보 가져오는게 가능하다.
        # queryset 객체는 리스트처럼 다룰 수 있다.
        return self.name