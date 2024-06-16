from django.db import models

# models.py 파일에 변경 사항이 생기면 마이그레이션이 필수!
#   makemigrations 명령어로 변경사항을 담은 migration을 만든다.
#   migrate 명령어로 변경사항을 DB에 적용시킨다.

class Post(models.Model):
    title = models.CharField('포스트 제목', max_length=100)
    content = models.TextField('포스트 내용')
    thumbnail = models.ImageField("썸네일 이미지", upload_to='post', blank=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    # 1대N 관계를 만들기 위해서는 N에 해당하는 Model에 ForeignKey를 정의하고, 1에 해당하는 Model과의 연결을 정의해야 한다.
    #   post는 글의 제목에 해당된다.
    #   즉 Comment를 생성하려면 어떤 Post에 연결될지 반드시 지정해줘야 한다.
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField('댓글 내용')

    def __str__(self):
        return f"{self.post.title}의 댓글 (ID: {self.id})"