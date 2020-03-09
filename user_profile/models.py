from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    '''扩展Django自带的User模型'''
    sex = models.IntegerField(verbose_name="性别", choices=((0, '男'), (1, '女')), default=0)
    phone = models.CharField(verbose_name="手机号", null=True, max_length=11)
    address = models.CharField(verbose_name="手机号", null=True, max_length=255)
    interest = models.CharField(max_length=255, null=True)
    image = models.ImageField(max_length=1000, upload_to='avatar', verbose_name=u'头像', blank=True,
                              default='avatar/default.jpg')
