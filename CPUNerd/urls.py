from django.urls import path
from CPUNerd import views
from CPUNerd.views import *

app_name = 'CPUNerd'

urlpatterns = [
    path('', index, name='index'),
    path('match/', MatchView.as_view(), name='match'),
]