from django.shortcuts import render
from django.http import HttpResponse
from CPUNerd.models import CpuModel
from django.views import View
from user_profile.views import LoginRequiredMixin

# Create your views here.

def index(request):
    cpu_obj_list = CpuModel.objects.all().order_by("-mark")[0:3]
    return render(request, 'cpunerd/index.html', {'obj': cpu_obj_list})


class MatchView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'cpunerd/match.html')

    def post(self, request):
        pass