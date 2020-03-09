from django.contrib import admin
from .models import CpuModel, CommentModel
# Register your models here.


class CpuModelAdmin(admin.ModelAdmin):
    list_display = ('description', 'image', 'mark', 'get_category_display', 'price', 'get_purpose_display', 'get_core_display', 'frequency')


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('cpu', 'user', 'content', 'create_time')



admin.site.register(CpuModel, CpuModelAdmin)
admin.site.register(CommentModel, CommentModelAdmin)