# 상세 페이지 기본 구조
- 전체 글 목록 페이지와 달리, 상세 페이지는 자신의 ID 값에 따라 서로 다른 동적인 ULR을 가져야 한다.
- 입력받은 ID에 해당하는 글의 상세 화면을 보여줄 수 있도록 동적인 URL이 필요하다.
  - ex. `/posts/{Post의 고유 ID}/`
- **상세 페이지와 같이 새 기능을 추가할 때**는 늘 아래와 같은 순서로 진행한다. (1~3번을 연결하는 작업)
  1. **View**
     - `views.py`에 함수 정의
     - 동적 URL을 불러오기 위한 키워드 변수 `post_id`를 함수의 인수로 추가한다.
        ```py
        # 예시
        def post_detail(request, post_id): 
            return render(request,"post_detail.html")
        ```
  2. **URL**
     - `urls.py`에 path 추가
     - ex. `path("posts/<int:post_id>/", post_detail)`
       - `<>` 사이의 값은 동적으로 값을 받을 수 있는 영역이다.
       - 그 안의 `:`으로 구분된 문자열의 왼쪽 값인 `int`는 정수 형태의 값을 받는다는 의미이다.
       - 오른쪽 값인 `post_id`는 해당 영역이 갖는 이름을 의미한다.
     - 동적으로 값을 받을 수 있는 패턴`<>`이 정의되어 있다면 패턴 부분에 해당하는 값, 즉 URLconf에 연결된 함수의 `post_id` 값을 View 함수로 전달하게 된다.
  3. **Template**
     - `templates` 디렉토리에 `post_detail.html` 파일을 새로 생성한다.
     - 상세 페이지 화면에 맞게 CSS 파일을 가져오고, 내비게이션 바를 만든다.

## View 함수가 호출되는 과정
1. 주소표시줄에 `/posts/10000/`를 입력, django의 개발서버로 요청을 전달한다.
2. **URLconf 확인**: 개발서버의 URLconf(`<master_app>/urls.py`)는 입력받은 URL이 어떤 경로에 해당하는지 파악한다.
   - `/posts/10000/`은 `/posts/<int:post_id>/` 패턴에 해당한다.
3. **View 확인**: 패턴에 연결된 View 함수로 요청(request)을 전달한다.
   - 이 과정에서 동적 패턴(`<>`)이 없다면 인수 없이 함수를 호출한다.
   - 지금과 같이 `<int:post_id>` 형태로 정의된 동적 패턴이 있다면 함수 호출 시 `post_id=전달받은 값`으로 인수를 전달한다.
4. (**Template**을 통해 전달받은 값을 확인 후 화면에 출력한다. → 아래 확인)

## 상세 페이지 ID 값에 해당하는 글 보여주기
### 전달받은 인수를 Template에 보여주기
- "상세 페이지 기본 구조"에서 알아본 내용을 통해, `<int:post_id>`로 URL에 동적인 값을 전달할 수 있게 되었다.
- URL을 통해 **ID 값을 전달받았음**을 Template, 즉 **사용자가 보는 화면에 출력**해야 한다.
1. View 함수에서 dict를 사용해 Template에 값을 전달한다.
   - `04_django_DB다루기`의 `View 함수로 가져온 데이터를 Template으로 전달하기` 내용 참고
  ```py
  # 예시
  def post_detail(request, post_id): 
      context = {
          "post_id": post_id,
      }
      return render(request,"post_detail.html", context)
  ```
1. Template에서 전달받은 값을 표시한다. (templates/post_detail.html)
  ```html
  <div id="post_detail">
      <h1>Post Detail</h1>
      <p>{{ post_id }}</p>
  </div>
  ```
### ID에 해당하는 Post 객체 가져오기
- 여기서 Post 객체는 `models.py`에 정의된 class를 의미한다.
    ```py
    class Post(models.Model):
        title = models.CharField("포스트 제목", max_length=100)
        content = models.TextField("포스트 내용")

        def __str__(self):
            return self.title
    ```
- class는 DB의 테이블 역할을 하며, class 안에 들어갈 정보들은 Django admin 또는 브라우저의 사용자 입력값으로 저장할 수 있다. (ft. `03_django_저장하기`)
- Post 객체는 Template 디렉터리의 HTML 파일에서 `{{ post.title }}`, `{{ post.content }}`와 같은 형태로 호출된다.
- `전달받은 인수를 Template에 보여주기`에서 전달받은 인수를 Template에 보여주는 단계까지 갔다면, 이젠 Post 객체를 가져와서 실제 Post가 출력해야 한다.
- ID에 해당하는 Post 객체를 가져오기 위해 View 함수와 Template의 수정이 필요하다.
1. View 함수에서 URL로 전달된 post_id값을 id로 갖는 Post를 (ORM을 사용해서) 가져온다.
   - id 값이 URL에서 받은 post_id값인 POST 객체를 가져온다.
  ```py
  # 예시
  def post_detail(request, post_id):
      post = Post.objects.get(id=post_id)
      context = {
          "post_id": post_id,
      }
      return render(request,"post_detail.html", context)
  ```
2. View 함수의 dict에서 post_id 매개변수로 전달된 값 대신 Post 객체를 전달한다.
  ```py
  # 예시
  def post_detail(request, post_id):
      post = Post.objects.get(id=post_id)
      context = {
          "post_id": post,
      }
      return render(request,"post_detail.html", context)
  ```
3. Template에서 아래와 같이 Post 객체를 사용하면, 브라우저에 해당 내용이 출력된다.
  ```html
  <div id="post_detail">
      <h1>{{ post.title }}</h1>
      <p>{{ post.content }}</p>
  </div>
  ```
4. 추가로 CSS를 이용해 스타일을 적용할 수 있다. (ex. navbar 등)

## 글 목록과 상세 페이지 연결
- 글 목록 페이지에서 각각의 글을 클릭해서 상세 페이지로 이동할 수 있도록 링크를 삽입한다.
- 상세 페이지의 id 값을 사용한 형태로, 각 글의 제목에 상세 페이지로의 이동 링크를 만들어 HTML 파일에 넣어준다.
  - 상세 페이지는 `/posts/<int:post_id>/` 형태의 URL을 갖는다.
  - 목록 페이지에서 상세 페이지로의 이동은 `/posts/{{ post.id }}/` 형태의 URL을 갖는다.
```html
{% for post in posts %}
    <li class = "post">
        <div>
            <a href="/posts/{{ post.id }}/"> {{ post.title }} </a>
        </div>
```