from django.db import models


# Create your models here.
class Users(models.Model):
    email = models.EmailField(verbose_name="이메일")
    password = models.CharField(max_length=128, verbose_name="비밀번호")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="가입일")
    rule = models.CharField(max_length=8, verbose_name='권한',
                            choices=(('admin', 'admin'), ('user', 'user')))

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
        verbose_name = "회원"
        verbose_name_plural = '회원 목록'
