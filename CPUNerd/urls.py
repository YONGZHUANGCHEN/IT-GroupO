from django.urls import path
from CPUNerd import views

app_name = 'CPUNerd'

urlpatterns = [
    path('', views.index, name='index'),
]