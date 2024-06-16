from django.shortcuts import render, redirect
from blog.models import Post, Comment

def post_list(request):
    # 모든 post 객체를 가진 queryset
    posts = Post.objects.all()
    # 템플릿에 전달할 dict
    context = {
        "posts": posts,
    }
    # 세번째 인수로 템플릿에 데이터를 전달
    return render(request, "post_list.html", context)

def post_detail(request, post_id):
    # id값이 URL에서 받아온 post_id값인 Post 객체
    post = Post.objects.get(id=post_id)

    # Template에서 form이 POST 요청을 한다.
    #   POST를 처리하기 위해서는 IF문을 활용해야 한다.
    if request.method == "POST":
        # Template의 textarea의 "name" 속성값("comment")을 가져온다.
        comment_content = request.POST["comment"]
        print(comment_content)

        Comment.objects.create(
            # Comment 모델은 Post 모델과 ForeignKey 관계로 연결되었기 때문에,
            #   Comment를 생성하려면 어떤 Post에 연결될지를 반드시 지정해줘야 한다!
            post=post,
            content=comment_content,
        )

    # (1) GET 요청으로 글 상세 페이지, or (2) POST 요청으로 댓글 생성 후 상세 페이지
    #   post_add처럼 redirect할 필요 없다!
    context = {
        # post_id 대신 Post 객체를 전달
        "post": post,
    }
    return render(request, "post_detail.html", context)

def post_add(request):
    # request.POST는 dict와 유사한 QueryDict 개체이며 csrf 태그가 번역된 hidden 유형의 input 값인 csrfmiddlewaretoken, 입력한 값인 title, content로 총 3개의 키값이 나타난다.
    # URL로 접근하면 GET 메서드의 요청으로 취급되므로, 이를 막기 위해 
    #   View에 POST 메서드의 요청이 전달되었을 때만 request.POST 데이터를 다루도록 if문 작성
    # form 태그에서는 GET, POST 방식만 사용할 수 있다.
    if request.method == "POST":
        # Template에서 form 태그의 "name" 속성으로 적은 값 (title, content..)
        title = request.POST["title"]
        content = request.POST["content"]
        thumbnail = request.FILES["thumbnail"]
        # ORM을 사용해서 DB에 데이터를 생성할 때는 create 메서드 사용 (shell에서도 가능)
        post = Post.objects.create(
            title=title,
            content=content,
            thumbnail=thumbnail,
        )

        # 글 작성을 완료했을 때 작성한 글의 상세 페이지로 이동하게 하는 redirect 함수
        return redirect(f"/posts/{post.id}")
    
    # else 일 경우 별도의 요청 작업이 없으므로 안적어도 상관없음
    # POST/GET 중 어느 요청이든 render 결과를 리턴한다.
    return render(request, "post_add.html")