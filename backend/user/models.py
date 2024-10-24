from django.db import models
from django.utils import timezone


# python manage.py makemigrations user
# python manage.py migrate
# Create your models here.
# 用户信息
class User(models.Model):
    name = models.CharField(max_length=20)  # 用户名
    username = models.CharField(max_length=200)  # 账号
    password = models.CharField(max_length=200)  # 密码
    email = models.EmailField(max_length=200)  # 邮箱
    create_time = models.DateTimeField(default=timezone.now)  # 创造时间

    def __unicode__(self):
        return self.username


class EmailCaptcheModel(models.Model):
    # 邮箱验证码检测
    email = models.CharField(max_length=200, verbose_name="邮箱")  # 邮箱
    captche = models.CharField(max_length=6, verbose_name="验证码")  # 邮箱验证码
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.email} - {self.captche}'
