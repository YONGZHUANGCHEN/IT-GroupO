from django.shortcuts import render
from django.http import HttpResponse
from CPUNerd.models import CpuModel

# Create your views here.

def index(request):
    cpu_obj_list = CpuModel.objects.all().order_by("-mark")[0:3]
    return render(request, 'cpunerd/index.html', {'obj': cpu_obj_list})
