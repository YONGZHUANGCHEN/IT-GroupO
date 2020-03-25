from django.db import models
from user_profile.models import UserProfile
# Create your models here.

#create cpu model
class CpuModel(models.Model):
    description = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(max_length=1000, upload_to='avatar', null=True, blank=True)

    mark = models.IntegerField()
    category = models.IntegerField(choices=((0, 'AMD'), (1, 'Intel')))
    price = models.IntegerField()
    purpose = models.IntegerField(choices=((0, 'Entertainment'), (1, 'office'), (2, 'Gaming and professional production')))
    core = models.IntegerField(choices=((0, 'four core'), (1, 'six core'), (2, 'eight core'), (4, 'ten core')))
    frequency = models.FloatField()
    label = models.CharField(max_length=100, default='i3')
    update_time = models.DateTimeField(auto_now=True)

#comment model
class CommentModel(models.Model):
    cpu = models.ForeignKey(CpuModel, verbose_name='cpu', on_delete=models.CASCADE, related_name='comment_list')
    user = models.ForeignKey(UserProfile, verbose_name='user', on_delete=models.CASCADE)
    content = models.CharField(verbose_name="comment", max_length=512)
    create_time = models.DateTimeField(auto_now_add=True)

#this is for new released model
class NewsModel(models.Model):
    title = models.CharField(verbose_name='title', max_length=255)
    image = models.ImageField(max_length=1000, upload_to='avatar', null=True, blank=True)
    content = models.TextField(verbose_name="content")
    create_time = models.DateTimeField(auto_now_add=True)





