from django.db import models


# Create your models here.

class TestUser(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name='사용자명')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    created_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name='등록일자')

    class Meta:
        db_table = 'testusers'


    def __str__(self):
        return self.username