# Model 구성하기

## DataBase 이해하기
### DataBase
- 엑셀의 스프레드시트와 같은 역할을 하는 데이터 관리 도구

### Model과 DataBase의 관계
- `02_django_사용하기`에서 URLconf를 메뉴판, View를 해당 메뉴를 처리하는 직원으로 가정했었다.
- Model은 메뉴를 만들기 위한 재료들을 저장하는 창고라고 가정한다.
  - 지속적으로 업데이트되는 메뉴 목록을 위해서는, 메뉴 정보를 저장할 수 있는 엑셀 시트가 필요하기 때문
- 파이썬의 함수로 View를 정의하듯, 파이썬의 클래스로 Model을 정의할 수 있다.
- 각각의 Model 클래스는 엑셀의 시트에 해당하고, 데이터베이스의 테이블에 해당한다
  - 엑셀의 Sheet ~ 장고의 Model ~ 데이터베이스의 Table

## App 만들기
- 이제 메뉴의 정보를 저장할 app을 추가해야 한다.
  - 장고에서는 큰 프로젝트를 app이라는 단위로 나눈다.
- 과정
  1. 새로운 app을 생성한다.
     1. `manage.py` 파일이 있는 곳에서 실행한다.
     2. `python manage.py startapp <app_name>`
  2. 명령을 실행하면 프로젝트에 `<app_name>`의 디렉토리가 추가 생성된다.
     1. `<app_name>` 안에는 `migrations` 디렉터리와 `__init__.py`, `admin.py`, `apps.py`, `models.py`, `tests.py`, `views.py` 파일이 생성된다.
     2. 파이썬 구조에서는 디렉터리는 곧 **패키지(package)**, 파일은 곧 **모듈(module)**이라고 부른다.
  3. app을 새로 생성하였으니, 장고에게 app 생성 사실을 알린다.
     1. project의 master 앱 안 `settings.py` 파일의 `INSTALLED_APPS` 리스트에 APP 이름을 추가한다.
     2. 생존신고와 같은 역할을 한다.

## Model 클래스 구현하기
- 새롭게 생성된 app에 정보를 저장할 수 있는 Model 클래스를 정의해야 한다.
- 과정
  1. `models.py`에 Model 클래스를 작성한다.
  2. Model 역할을 하는 클래스를 만들 때는 장고에 내장된 `models.Model` 클래스를 반드시 상속받아야 한다.
     1. `from django.db import models` (기본으로 설정되어 있음)
  3. 장고에서 제공하는 `models.Model` 클래스를 통해, **데이터베이스에서 하나의 테이블 형태**를 구현하게 된다.
  4. Model 클래스에서 데이터 유형을 지정하는 것은 엑셀에서 시트의 특정 열이 날짜나 숫자, 통화를 나타내도록 설정하는 것과 유사하다.

## DataBase 마이그레이션의 생성과 적용
- 새롭게 생성한 App, Model은 동작을 위한 데이터베이스를 필요로 한다.
- 장고는 개발용으로 쉽게 사용 가능한 SQLite라는 파일 기반의 데이터베이스를 내장하고 있다.
- SQLite로 데이터베이스를 하나의 파일로써 관리할 수 있다.
- 과정
  1. 데이터베이스 마이그레이션을 통해, 테이블을 생성하고 그 안에 데이터를 넣는다.
     1. 마이그레이션은 하나의 App 단위로 생성된다.
     2. 마이그레이션을 하지 않으면 개발서버(runserver)가 동작하지 않는다.
  2. 아래와 같이 마이그레이션 파일을 생성한다.
     1. `python manage.py makemigrations <클래스가 속한 app_name>`
  3. 아래와 같이 마이그레이션 파일을 데이터베이스에 적용한다.
     1. `python manage.py migrate <클래스가 속한 app_name>`
     2. `migrate`는 위에서 실행한 마이그레이션을 적용하는 명령어이다.
     3. 그냥 `python manage.py migrate`만 하게 되면, 장고에 내장된 기본 기능들이 마이그레이션 적용된다.
  4. SQLite에 테이블이 생성되고, Model에서 작성했던 필드 외에 장고에서 각 행을 식별할 수 있도록 자동으로 생성해주는 id 열도 함께 만들어진다.
  5. Model 클래스를 생성하는 경우 말고 변경하는 경우에도 같은 과정을 반복한다.
     1.  `python manage.py makemigrations <클래스가 속한 app_name>`
     2.  `python manage.py migrate <클래스가 속한 app_name>`

# Django admin 사용하기
- 장고는 개발자나 사이트 이용자들이 쉽게 데이터를 편집할 수 있는 관리자 페이지 Django admin을 제공한다.
- Django admin은 자타공인 장고의 가장 강력한 기능 중 하나이다.
- 과정
  1. admin을 필요로 하는 App 패키지(디렉터리)에 들어온다.
  2. `admin.py` 파일을 새로 생성한다.
  3. `from django.contrib import admin`
  4. `from .models import <app_name>`
  5. `class <app_name>Admin(admin.ModelAdmin):`
  6. `manage.py`를 사용하여 관리자 페이지에 들어가는 계정을 직접 생성한다. (Username, Password)
  7. `python manage.py createsuperuser`
  8. 생성한 사용자 계정으로 관리자 페이지(localhost:8000/admin/)에 접속한다.
  9. 이전에 생성했던 App 안의 Model로 만들어진 데이터베이스 테이블 페이지를 연다.
  10. 해당 페이지에서 데이터를 추가 및 관리할 수 있다.
      1. 관리자 페이지에서 데이터를 추가했을 때, 각 클랙스 객체를 더 자세히 알아볼 수 있도록 추가 설명을 작성할 수도 있다.
      2. 해당 class 함수 내부에 아래와 같이 `__str__` 메서드를 추가한다.
          ```py
          def __str__(self):
            return self.<class 내부에 정의한 속성 중 관리자 페이지되었으면 하는 속성>
          ```

