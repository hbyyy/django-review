import re

from django.db import models

from core.models import TimeStampModel


class Board(TimeStampModel):
    TAG_PATTERNS = re.compile(r'#(\w+)')

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

    def _save_tags(self):
        tags_name_all = set(re.findall(self.TAG_PATTERNS, self.contents))
        tags = []
        for tag in tags_name_all:
            tags.append(Tag.objects.get_or_create(name=tag)[0])
        self.tags.set(tags)

    def save(self, *args, **kwargs):
        super(Board, self).save(*args, **kwargs)
        self._save_tags()


class Tag(TimeStampModel):
    name = models.CharField(max_length=64, verbose_name='태그명')

    class Meta:
        db_table = 'tags'
        verbose_name = '태그'
        verbose_name_plural = '태그'

    def __str__(self):
        return f'{self.name}, board_count : {self.boards.count()}'
