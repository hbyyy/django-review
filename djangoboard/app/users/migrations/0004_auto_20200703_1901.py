# Generated by Django 3.0.8 on 2020-07-03 10:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_testuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testuser',
            name='created_date',
        ),
        migrations.AddField(
            model_name='testuser',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='생성일자'),
            preserve_default=False,
        ),
    ]