from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from CPUNerd.models import CpuModel, CommentModel
from django.views import View
from user_profile.views import LoginRequiredMixin

# Create your views here.


def index(request):
    cpu_obj_list = CpuModel.objects.all().order_by("-mark")
    return render(request, 'CPUNerd/index.html', {'obj': cpu_obj_list})


class MatchView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'CPUNerd/match.html')

    def post(self, request):
        pass


class CpuDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        obj = CpuModel.objects.get(id=int(kwargs['id']))
        last_obj = next_obj = None
        tem = CpuModel.objects.filter(id__lt=obj.id).values_list('id', 'content').order_by(
            "-id")
        if tem:
            last_obj = tem[0]
        tem = CpuModel.objects.filter(id__gt=obj.id).values_list('id', 'content').order_by(
            "id")
        if tem:
            next_obj = tem[0]
        return render(request, 'CPUNerd/cpu_detail.html', {'obj': obj, 'last_obj': last_obj, 'next_obj': next_obj})

    def post(self, request):
        pass


class CommentView(LoginRequiredMixin, View):
    def post(self, request):
        cpu_id = request.GET.get("id")
        obj = CpuModel.objects.get(id=int(cpu_id))
        CommentModel.objects.create(user=request.user,cpu=obj,content=request.POST.get("remark", ""))
        return redirect(reverse('CPUNerd:cpu_detail', kwargs={'id': cpu_id}))