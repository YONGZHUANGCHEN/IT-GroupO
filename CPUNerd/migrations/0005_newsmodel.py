# Generated by Django 2.0.3 on 2020-03-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPUNerd', '0004_auto_20200309_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('image', models.ImageField(blank=True, max_length=1000, null=True, upload_to='avatar')),
                ('content', models.TextField(verbose_name='content')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
