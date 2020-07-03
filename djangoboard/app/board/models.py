from django.db import models


# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=64,
                             verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('users.TestUser', on_delete=models.CASCADE,
                               verbose_name='작성자')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='작성일자')

    class Meta:
        db_table = 'board'
        verbose_name = '게시글'
        verbose_name_plural = '게시글'

    def __str__(self):
        return self.title
