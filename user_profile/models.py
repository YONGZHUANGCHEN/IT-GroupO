from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    #create models for the user profile, use the models from django.
    sex = models.IntegerField(verbose_name="Gender", choices=((0, 'Male'), (1, 'Female')), default=0)
    phone = models.CharField(verbose_name="Phonenumber", null=True, max_length=11)
    address = models.CharField(verbose_name="Phonenumber", null=True, max_length=255)
    interest = models.CharField(max_length=255, null=True)
    image = models.ImageField(max_length=1000, upload_to='avatar', verbose_name=u'avatar', blank=True,
                              default='avatar/default.jpg')
