# ForeignKey(외부키) 연결
- 글 상세 페이지인 Post 모델이 존재한다.
- 글 하단에 달리는 댓글 기능은, 반드시 어떠한 글(Post)에 소속되어야 한다.
- 댓글 작성 기능인 Comment 모델을 생성한다.
  - Comment를 생성하려면, 반드시 어떤 Post에 연결될지 지정해주어야 한다.
  - Comment 모델은 Post 모델과 ForeignKey 관계로 연결되어 있다.
    ```py
    class Comment(models.Model):
        post = models.ForeignKey(Post, on_delete=models.CASCADE)
        content = models.TextField("댓글 내용")
    ```

## 새로 생성된 Comment 모델을 연결하기
### (1) 댓글 생성 form을 Template에 추가한다.
- 추가적으로, Comment 모델 생성 이후 댓글 생성 form을 Template에 추가하는 방법은 아래와 같다.
  - `{% csrf_token %}` 적용
  - form의 method로 "POST" 적용
  - textarea에 "name" 속성 지정
  - button에 class 지정 및 CSS 스타일 적용
    ```HTML
    <form method="POST">
        {% csrf_token %}
        <textarea name="comment"></textarea>
        <button type="submit" class="btn btn-primary"> 댓글 작성 </button>
    </form>
    ```
### (2) View에서 Comment를 생성한다.
```py
# 예시
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method = "POST":
        comment_content = request.POST["comment"]
        # Comment 객체 생성
        Comment.objects.create(
            post=post,
            content=comment_content,
        )
    # GET 요청으로 상세 페이지를 보여주든, POST 요청으로 댓글을 생성하든,
    # 두 경우 모두 이 글의 상세 페이지를 보여주면 된다.
    context = {
        "post_id": post,
    }
    return render(request,"post_detail.html", context)
```