# 데이터베이스 전체 목록 가져오기
- View는 주문을 처리하는 직원이고, Model은 메뉴의 재료를 저장하는 창고이다.
- 각각의 Model 클래스는 데이터베이스의 테이블에 해당한다
- View 함수가 데이터베이스의 테이블 목록을 동적으로 보여줄 수 있도록 한다.
- 과정
  1. 파이썬 인터프리터(소스 코드를 바로 실행하는 프로그램 또는 환경)를 실행시킨다.
  2. `python manage.py shell`
  3. Model 클래스의 object 속성을 사용해서 데이터베이스 테이블의 데이터를 가져올 수 있다.
  4. `from .models import <app_name>`
  5. object의 all()을 호출해서 테이블의 전체 데이터를 가져온다.
  6. `<app_name>.objects.all()`
  7. 결과값으로 QuerySet이라는 객체가 출력된다.
  8. 해당 객체의 내부 속성으로 데이터들을 확인할 수 있다.


# 데이터베이스에서 특정 조건을 만족하는 데이터 정보 가져오기
- 조건을 주어 해당하는 데이터만 가져올 수도 있다. (낱개, 여러개 모두 가능)
- 과정
  1. 파이썬 인터프리터(소스 코드를 바로 실행하는 프로그램 또는 환경)를 실행시킨다.
  2. `python manage.py shell`
  3. `from .models import <app_name>`
  4. object의 get() 메서드로 조건에 부합하는 객체 하나를 가져와서 해당 데이터를 확인할 수 있다.
  5. `<app_name>.objects.get(<class에 정의된 속성)="<해당 속성의 데이터값>"`
  6. object의 filter() 메서드로 조건에 부합하는 여러 객체를 가져올 수 있다.
     1. ex. `<app_name>.objects.filter(<속성>__endswith="<데이터>")`
     2. `<속성>__contains="<데이터>"` ⇒ 속성에 데이터가 포함된 경우를 조회
     3. `<속성>__exact="<데이터>"` ⇒ 속성과 데이터가 정확히 일치하는 경우를 조회
  7. all()이나 filter()를 사용하여, DB에 요청한 조건에 해당하는 객체를 하나가 아닌 목록으로 받을 때는 객체를 담는 리스트 역할을 하는 QuerySet 객체가 출력된다.
  8. QuerySet 객체를 변수에 담아서 리스트처럼 다룰 수 있다.
  9.  QuerySet 내의 객체는 <app_name>의 인스턴스 타입을 갖는다.


# View 함수에서 데이터를 가져오는 과정
1. 사용자가 브라우저에 URL을 입력하여 원하는 데이터를 요청한다.
2. URLconf는 전달받은 URL을 해석하여 요청에 해당하는 View 함수를 실행한다.
3. View 함수는 Model 클래스를 통해 데이터베이스에서 데이터를 가져온다.
4. View 함수는 가져온 데이터를 Template에게 전달한다.
5. Template은 View에게 전달된 데이터를 사용해 동적인 HTML을 생성한다.
6. 생성한 HTML은 View 함수의 return에 의해 브라우저로 돌아가 사용자에게 보여진다.

## View 함수에서 데이터 가져오기 (3번 과정)
1. `views.py`에서 `from .models import <app_name>` 가져온다. (아래 예시 참고)
  ```py
  from .models import Burger

  def burger_list(request):
      burgers = Burger.objects.all()
      print("전체 햄버거 목록:", burgers)
      return render(request, "burger_list.html")
  ```
2. `burgers = Burger.objects.all()` ⇒ 전체 햄버거 데이터를 데이터베이스로부터 가져온다.
3. `print(burgers)` ⇒ 가져온 데이터를 개발서버가 실행되는 화면에 출력한다.
4. `return render` ⇒ View 함수에서 Template의 HTML 파일을 브라우저에 돌려줄 수 있게 한다.
5. `burger_list.html` ⇒ Template의 내용을 사용자에게 돌려준다.

## View 함수로 가져온 데이터를 Template으로 전달하기 (4번 과정)
- View 함수는 Model 클래스를 사용해 데이터베이스로부터 원하는 데이터를 가져오고, 이를 Template으로 전달해준다.
- Template은 View 함수가 전달해준 데이터를 사용해서 HTML을 동적으로 구성한다.
- 즉, 사용자의 요청이나 데이터베이스의 데이터에 따라 다른 HTML을 그때그때 만들어서 보여준다.
- Template으로 가져온 데이터를 전달할 때는 파이썬의 딕셔너리(dictionary) 객체를 사용해서 전달한다.
- `render`의 세번째 인자로, Template에 전달할 dict 객체를 넣어준다.
- `render(request, "burger_list.html", {"burgers": burgers})`
  - burgers 키에 burgers 변수를 전달한다.
  - burgers 변수는 `Burger.objects.all()`을 실행한 결과인 QuerySet의 객체이다.

## Template에서 데이터 다루기 (5, 6번 과정)
- HTML의 형태를 가진 Tempalte에서 변수를 출력할 때는 `{{ }}` 사이에 변수명을 입력한다.
- HTML에서 태그는 `{% %}` 사이에 입력된다. (장고 템플릿 내장 태그)
  - HTML의 태그 내에서는 줄바꿈을 하여도 페이지에 표시되진 않는다.
- 파이썬에서의 for 문 사용법은 아래와 같다.
    ```py
    for item in objects:
        print(item)
    ```
- Template에서의 for 문 사용법은 아래와 같다.
    ```py
    {% for item in objects %}
        <div>{{ item }}</div>
    {% endfor %}
    ```
- View 함수 dict의 키(key) 값은 Template의 변수가 된다. (ex. burgers)
- Template에서 `{{ }}` 내부 변수값으로 불러와서 브라우저에 출력할 수 있다.
- 변수를 그냥 출력하면 사용자에게 QuerySet 형태로 보여진다.
- 때문에 {% for %} 태그를 사용해서 객체를 순회하며 변수를 출력한다.
- 객체의 속성을 따로따로 표시하기 위해 아래와 같이 작성한다.
    ```py
    {% for burger in burgers %}
        <div>
            {{ burger.name }}
            (가격: {{ burger.price }}원,
            칼로리: {{ burger.calories }}kcal)
        </div>
    {% endfor %}
    ```