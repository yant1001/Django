# 웹에서 데이터를 전송하는 방법
- 웹 브라우저에서 서버에 데이터를 보내는 방법에는 GET과 POST 방식이 있다.

### GET 방식으로 데이터 전송하기
- 서버에 보낼 데이터가 공개되어도 상관없는 경우에 사용한다.
- 주소표시줄에 데이터가 그대로 공개된다.
- 예를 들어, 특정 검색어의 결과를 보고 싶은 경우 서버에 그 단어를 검색한다는 사실을 알려야 하므로 데이터가 공개되는 경우에 해당한다.

### POST 방식으로 데이터 전송하기
- 외부에 노출되어서는 안 되는 비밀값이 데이터가 될 때 사용한다.
- 주소표시줄을 통하지 않고, 요청 자체에 데이터를 담아서 서버에 보낸다.
- 예를 들어, 로그인 과정에서 서버에 전송하는 아이디와 비밀번호는 숨겨져야 하므로 POST 방식을 통해 별도의 데이터로 처리하여 전송한다.


# GET 방식을 사용하여 특정 단어 검색
## 1. 장고를 사용해 새로운 페이지 생성 후 연결까지 구현
1. View 함수를 추가 생성한다. (메뉴를 처리하는 직원을 구현)
   1. `return render(request, "<연결할 HTML 파일>")`
   2. 필요에 따라 render의 세번째 인자로 `<변수값 dict>`를 추가할 수도 있다.
2. View의 처리 결과를 보여줄 Template의 HTML 파일을 작성한다. (만든 메뉴를 사용자에게 보여주는 방식을 구현)
3. URLconf에 새로운 path를 추가한다. (메뉴판에 새로운 메뉴를 추가)
   1. ex. `path("search/", views.burger_search)`
   2. `"search/"` ⇒ 사용자가 검색 페이지로 들어올 수 있는 URL 주소
   3. `views.burger_search` ⇒ `views.py`에 정의된 View 함수 선택 (일반적으로 함수에 연결된 HTML 파일과 이름이 동일하다.) 
4. 개발서버(runserver)를 실행하여 path에 추가한 경로로 접근하면 HTML 파일에 작성한 Template 내용을 확인할 수 있다.

## 2. View에 데이터 전달
- 주소표시줄의 URL을 이용해서 직접 데이터를 전달한다.
- 아직 개발서버의 로그로는 데이터가 출력되지만, 브라우저에는 검색 결과가 출력되지 않고 있는 단계이다.
- GET 방식을 사용하면 URL의 끝에 `?`를 붙이고 `key=value` 형태로 서버에 데이터를 전송할 수 있다.
- 사용자가 서버에 전달한 데이터는 View 함수의 첫번째 인자인 request의 GET 속성으로 전달된다.
  - `request.GET`은 QueryDict 객체이며, 이의 키(key)에 사용자가 검색한 데이터가 들어있다.
```py
# 예시
def burger_search(request):
    keyword = request.GET.get("keyword")

    # 이름(name 속성)에 전달받은 키워드 값이 포함된 Burger를 검색한다.
    burgers = Burger.objects.filter(name__contains=keyword)

    return render(request, "burger_search.html")
```

## 3. Template에서 데이터 출력
- 개발서버의 로그에 출력된 값을 Template에 객체로 전달해서 브라우저에서 보여주는 단계이다.
- 1-1-2번에서 언급한 바와 같이, render의 세번째 인자로 dict 객체를 전달한다.
- 이로써 속성(ex. name 속성)에 GET 방식으로 전달받은 키워드가 속성에 포함된 목록을 dict 변수 이름으로 템플릿에서 사용할 수 있게 된다.


# form을 사용한 GET 요청
## 1. 에러가 날 경우를 대비해 코드 수정
- 상기 작성된 'GET 방식을 사용하여 특정 단어 검색' 과정을 HTML의 form을 사용하여 좀 더 간편하게 동작시킬 수 있다.
- 상기 과정만 진행한 경우, 만약 request.GET이라는 dict 안에 keyword라는 키가 없다면 keyword 변수에는 검색어 문자열 객체 대신 None 객체가 할당된다.
- if 문을 이용하여, key 값이 없다면 검색을 하지 않도록 코드를 작성할 수 있다.
```py
if keyword is not None:
    burgers = Burger.objects.filter(name__contains=keyword)
else:
    burgers = Burger.objects.none()
```

## 2. Template에 검색창 생성
- 특정 단어를 검색하는 HTML 페이지에 검색창과 버튼을 추가한다.
  - HTML에서 사용자 입력을 받는 요소는 `<input>`, 버튼은 `<button>` 태그를 이용한다.
  - `<input>`은 단일 태그이다.
- 사용자가 입력한 데이터를 브라우저가 처리할 수 있도록 form 태그를 작성한다.
```py
<form method="GET">
    <input type="text" name="keyword">
    <button type="submit">검색</button>
</form>
```
- `<form method="GET">` ⇒ 데이터를 GET 방식으로 전달
- `<input type="text" name="keyword">` ⇒ 사용자 입력을 받는 검색창으로, 입력된 값은 keyword라는 항목으로 전달
- `<button type="submit">검색</button>` ⇒ 버튼 모양을 만들어주는 태그로, 데이터를 제출하기 위한 목적임을 type으로 나타냄



# POST 방식을 사용한 데이터 전송
## 1. View에 데이터 전달
- GET 메서드로 보낸 데이터는 `request.GET`에 담겨오고, POST 메서드로 보낸 데이터는 `request.POST`에 담겨온다.
- 주소표시줄에 직접 URL을 작성하여 접속한다면 GET 메서드의 요청으로 취급되므로, POST 메서드의 요청이 전달될 때는 `request.POST`의 데이터들을 다루도록 if-else 구문을 작성한다.
- 다만, GET 요청인 경우인 else문은 따로 선언하지 않고 GET/POST 요청 모두에서 마지막에 render 함수 결과를 반환하도록 하면 코드가 깔끔해진다.
  ```PY
  def post_add(request):
    if request.method == "POST":
      title = request.POST['title']
      content = request.POST['content']
    return render(request, "post_add.html")
  ```

- 주소표시줄의 URL을 이용해서 직접 데이터를 전달한다.
- 아직 개발서버의 로그로는 데이터가 출력되지만, 브라우저에는 검색 결과가 출력되지 않고 있는 단계이다.
- GET 방식을 사용하면 URL의 끝에 `?`를 붙이고 `key=value` 형태로 서버에 데이터를 전송할 수 있다.
- 사용자가 서버에 전달한 데이터는 View 함수의 첫번째 인자인 request의 GET 속성으로 전달된다.
  - `request.GET`은 QueryDict 객체이며, 이의 키(key)에 사용자가 검색한 데이터가 들어있다.
```py
# 예시
def burger_search(request):
    keyword = request.GET.get("keyword")

    # 이름(name 속성)에 전달받은 키워드 값이 포함된 Burger를 검색한다.
    burgers = Burger.objects.filter(name__contains=keyword)

    return render(request, "burger_search.html")
```

## 3. Template에서 데이터 출력
- 개발서버의 로그에 출력된 값을 Template에 객체로 전달해서 브라우저에서 보여주는 단계이다.
- 1-1-2번에서 언급한 바와 같이, render의 세번째 인자로 dict 객체를 전달한다.
- 이로써 속성(ex. name 속성)에 GET 방식으로 전달받은 키워드가 속성에 포함된 목록을 dict 변수 이름으로 



# form을 사용한 POST 요청
- **GET 메서드**를 사용한 전송 방법은 URL로 데이터를 전달하기 때문에 주소표시줄에 데이터가 그대로 나타난다.
- **POST 메서드**를 사용하면 URL을 통하지 않고 더 많은 데이터를 제약 없이 보낼 수 있다.
- `<form>` 태그의 method 속성을 정의할 때 POST를 입력한다.
- POST 요청을 하는 form에는 반드시 `{% csrf_token %}` 태그를 넣어야 한다.
  - 오류없이 POST 요청을 하기 위해서는 **CSRF** 인증이 필수적이다.
  - CSRF: Cross-Site Request Forgery (사이트 간 요청 위조)
  - CSRF 공격 방어의 핵심은 **로그인한 사용자가 의도하지 않은 POST 요청을 거부**하는 것이다.
  - Template의 HTML 파일에서 `{% csrf_token %}` 태그를 사용하면, 태그를 사용한 영역을 **브라우저별로 구분되는 값**(=CSRF token)으로 치환하기 때문에, POST 요청을 안전하게 수락할 수 있게 된다.
  ```HTML
  <h1> Post Add </h1>
  <form method="POST">
      {% csrf_token %}
      <div>
  ```
- GET 방식으로는 CSRF 인증 오류가 발생하지 않았던 이유는, GET/POST에 따라 Django가 데이터를 처리하는 방식이 다르기 때문이다.
  - GET 방식의 요청: 사이트의 특정 페이지에 접속, 검색 등의 **읽기/조회** 행동 수행
  - POST 방식의 요청: 사이트의 특정 데이터를 **작성/변경** 행동 수행
  - Django는 POST 요청에 대해 GET 요청보다 높은 보안 수준을 적용한다.