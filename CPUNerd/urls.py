from django.urls import path
from CPUNerd import views
from CPUNerd.views import *

app_name = 'CPUNerd'

urlpatterns = [
    path('', index, name='index'),
    path('match/', MatchView.as_view(), name='match'),
    path('rank/', RankView.as_view(), name='rank'),
    path('cpu-detail/<int:id>', CpuDetailView.as_view(), name='cpu_detail'),
    path('comment/', CommentView.as_view(), name='comment'),
]