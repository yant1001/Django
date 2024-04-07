# Django 사용하기
- 장고 설치 후, 새로운 프로젝트를 생성한다.
  - `django-admin startproject <project_name>`
- 프로젝트 안에는 `<project_name>`과 동일한 이름의 `master app`이 존재한다.


## View 사용하기
- View를 햄버거 가게에서 주문을 처리하는 직원으로 가정한다.
- 직원(View)이 손님(Request)으로부터 요청받은 메뉴를 만들어서 제공하는 과정을 함수로 정의하여 처리한다.
- 과정
  1. `views.py` 파일을 새로 생성한다.
  2. 특정 페이지를 제공하는 View 함수를 만든다. (ex. `def main(request):`)
  3. 장고의 view 함수에서 브라우저에 텍스트를 돌려주고 싶다면 언제나 **HttpResponse 객체** 안에 담아서 리턴해줘야 한다. (문자열을 직접 리턴X)
     1. HttpResponse는 장고가 돌려준 값을 브라우저가 읽을 수 있도록 처리해준다.
     2. 이 때 templates 디렉터리의 html 파일을 생성하여 작성 후, 이 주소를 리턴값으로 사용할 수 있다.
     3. view 함수 정의 완료
  4. **손님(Request)**과 **주문을 처리하는 직원(View)**을 연결해주는 **주문을 받는 직원(URLconf)**을 만들어야 한다.
  5. URLconf(주문을 받는 직원)는 손님이 메뉴 요청할 때 메뉴판 안내 역할을 한다.

## URLconf 구현하기
- URLconf를 햄버거 가게에서 손님이 메뉴를 요청할 때 안내하는 메뉴판 역할의 주문 받는 직원으로 가정한다.
- 과정
  1. 프로젝트를 생성할 때 기본으로 만들어져 있는 `urls.py` 파일을 연다.
  2. 파일 내 `urlpatterns`라는 리스트의 path 항목은 메뉴를 나타낸다.
  3. 기본적으로 `path('admin/')`라는 관리자 페이지 주소가 정의되어 있다.
  4. view 파일에서 만들어낸 주문을 처리하는 직원을 path 함수를 사용해서 연결시킨다.
     1. `from . import views`과 같이 view 파일 전체를 연결할 수 있다.
     2. `from <project_name>.views import <function_name>`과 같이 특정 view 함수만 연결할 수 있다.
  5. path 함수에서, view 함수에서의 이름(직원이름)과 URLconf에서의 이름(메뉴명)이 같지 않아도 된다.
     1. ex. `path('list/', views.board_list)`
     2. ex. `path('burgers/', views.burger_list)`

## Template 사용하기
- Template은 장고가 브라우저에 보낼 문서의 형태를 미리 만들어놓은 것이다.
  - 웹 브라우저에 보내는 문서 형식인 HTML을 이용해서 많은 내용을 저장한다.
- 요청을 처리하는 함수인 **View**와, 처리해서 브라우저에 보내줄 내용을 (HTML 파일에) 미리 담아놓은 **Template**을 분리해서 사용한다
- HTML은 웹 페이지 표시를 위해 개발된 마크업 언어이다.
  - 문서나 데이터의 구조를 명기하는 언어인 마크업은 대표적으로 HTML과 XML이 있다.
  - `<div>내용</div>`와 같이 열고 닫는 태그 형태가 있다.
  - `<img src='이미지 주소'>`와 같이 단독으로 쓰이는 태그 형태가 있다.
- 과정
  1. 최상위 경로(project 디렉터리)에 `temlplates` 디렉터리를 새로 생성한다.
     1. project 디렉터리의 master 앱 안에 생성할 수도 있지만, 별도 변수 생성이 필요하다.
     2. project의 master 앱은 project와 동일한 이름으로 초기 생성된다.
     3. project 이름은 생성 이후 변경 가능하지만, master 앱의 이름은 변경하면 안된다.
  2. `temlpaltes` 디렉터리 안에 사용자에게 보여줄 내용을 담은 HTML 파일들을 작성한다. 
  3. master 앱 `settings.py` 안에 있는 `templates` 디렉터리를 장고가 인식할 수 있도록 설정한다.
     1. master 앱의 `settings'py`에 들어간다.
     2. `TEMPLATES = [`로 시작하는 코드를 찾는다.
     3. `'DIRS': []` 사이에 `BASE_DIR / 'templates'`를 넣어준다.
        1. 별도로 `TEMPLATES_DIR` 변수를 생성해서 `'DIRS': [TEPLATES_DIR]` 형태로 넣어주는 방법도 있다.
        2. TEMPLATES 아래의 'DIRS' 리스트의 경로는 장고가 Template을 찾는 디렉터리들이다.
        3. `BASE_DIR`은 프로젝트 최상위 경로의 디렉터리를 가리킨다.
  4. View 함수에서 Template의 HTML 파일을 브라우저에 돌려줄 수 있도록 `views.py`에서 render 함수를 import 한다.
     1. `from django.shortcuts import render`
     2. view에서 함수 정의(def) 시 `return render(request, 'main.html)` 형태로 render 함수를 사용할 수 있다.
     3. render 함수의 첫번째 인수(argument)로는 View 함수에 자동으로 전달되는 request 객체를 지정한다.
     4. 두번째 인수로는 Template의 경로를 지정한다.
     5. Template의 경로는 `settings.py`에서 지정한 DIRS 설정의 templates 디렉터리 경로를 기준으로 작성한다.
  5. [참고] 새로운 app을 생성하면 `urls.py` 파일과 `templates` 디렉터리를 새로 생성해서 사용해야 한다.



# Django 생성 순서 정리
## 프로젝트 생성
- `django-admin startproject <project_name>`
## 앱 생성
- (<project_name>/<app_name> 구현)
1. 새로운 app 생성 `python manage.py startapp <app_name>`
2. 생성 app 등록 in `<project_folder>/intro/settings.py/INSTALLED_APPS`
   1. 앱을 생성하면 무조건 master 앱의 `settings.py/INSTALLED_APPS`에 출생신고를 해야 한다.
3. (urls.py 새로 생성)
4. 특정 URL 접두사 사용 주소로 포워딩(include) in `intro/urls.py/urlpatterns`
5. 새로 생성한 `app/views.py` 에서 `def` 함수 정의
6. 새로 생성한 `app/urls.py/urlpatterns` 에서 `path` 함수 입력
7. 미리 입력한 html 이름에 맞춰 `project_folder/app/templates` 내 html 파일 생성
8. html 파일에 출력될 내용 작성
9.  프로젝트 폴더에서 개발서버(런서버) 페이지 실행 `python manage.py runserver`