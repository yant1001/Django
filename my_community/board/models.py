from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')

    # User 테이블의 pk와 Foreign Key로 연결
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='작성자')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성시간')

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'tb_board'