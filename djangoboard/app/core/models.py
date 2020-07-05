from django.db import models


# Create your models here.


class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='생성일자')

    class Meta:
        abstract = True
