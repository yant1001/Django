from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    # __str__ 메소드
    #   관리자 페이지에서, User 객체의 이름을 원하는 문자열로 표시할 수 있다.
    def __str__(self):
        return self.email
    
    # Meta 클래스
    #   해당 모델과 DB의 특정 테이블을 연결하고 싶을 때 사용하므로, 모델의 내부 클래스로 구성된다.
    #   현재 만들고 있는 모델의 내용이 어떤 DB의 어떤 테이블에 만들어져야 할지 알려준다.
    class Meta:
        db_table = 'tb_user'
        # verbose~ ⇒ 관리자 페이지에서 모델을 표시하기 위한 항목들
        #   verbose_name: 영어권에서 단수의 표시
        #   verbose_name_plural: 영어권에서 복수의 표시
        verbose_name = '사용자'
        verbose_name_plural = '사용자'