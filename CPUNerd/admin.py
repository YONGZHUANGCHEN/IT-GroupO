from django.contrib import admin
from .models import CpuModel
# Register your models here.


class CpuModelAdmin(admin.ModelAdmin):
    list_display = ('description', 'image', 'mark', 'get_category_display', 'price', 'get_purpose_display', 'get_core_display', 'frequency')

admin.site.register(CpuModel, CpuModelAdmin)