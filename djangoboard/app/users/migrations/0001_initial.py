# Generated by Django 3.0.8 on 2020-07-02 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='사용자명')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='등록일자')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
