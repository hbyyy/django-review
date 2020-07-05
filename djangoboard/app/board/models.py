from django.db import models

# Create your models here.
from core.models import TimeStampModel


class Board(TimeStampModel):
    title = models.CharField(max_length=64,
                             verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('users.TestUser', on_delete=models.CASCADE,
                               verbose_name='작성자')
    tags = models.ManyToManyField('board.Tag', verbose_name='태그', related_name='boards')

    class Meta:
        db_table = 'boards'
        verbose_name = '게시글'
        verbose_name_plural = '게시글'

    def __str__(self):
        return self.title


class Tag(TimeStampModel):
    name = models.CharField(max_length=64, verbose_name='태그명')

    class Meta:
        db_table = 'tags'
        verbose_name = '태그'
        verbose_name_plural = '태그'

    def __str__(self):
        return f'{self.name}, board_count : {self.boards.count()}'
