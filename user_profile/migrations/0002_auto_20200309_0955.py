# Generated by Django 2.0.3 on 2020-03-09 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='avatar/default.jpg', max_length=1000, upload_to='avatar', verbose_name='头像'),
        ),
    ]