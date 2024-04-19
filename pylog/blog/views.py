from django.shortcuts import render
from blog.models import Post

def post_list(request):
    # 모든 post 객체를 가진 queryset
    posts = Post.objects.all()
    # 템플릿에 전달할 dict
    context = {
        "posts": posts,
    }
    # 세번째 인수로 템플릿에 데이터를 전달
    return render(request, "post_list.html", context)