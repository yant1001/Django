from django.db import models

class Post(models.Model):
    title = models.CharField('포스트 제목', max_length=100)
    content = models.TextField('포스트 내용')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    # 1대N 관계를 만들기 위해서는 N에 해당하는 Model에 ForeignKey를 정의하고, 1에 해당하는 Model과의 연결을 정의해야 한다.
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField('댓글 내용')

    def __str__(self):
        return f"{self.post.title}의 댓글 (ID: {self.id})"