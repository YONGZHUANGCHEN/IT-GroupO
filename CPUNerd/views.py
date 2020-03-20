from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from CPUNerd.models import CpuModel, CommentModel, NewsModel
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
        obj = CpuModel.objects.all()
        core = request.POST.get('core', '')
        min_price = request.POST.get('min_price', 0)
        max_price = request.POST.get('max_price', 0)
        purpose = request.POST.get('purpose', '')
        label = request.POST.get('label', '')
        if core:
            obj = obj.filter(core=int(core))
        if min_price:
            obj = obj.filter(price__gte=int(min_price))
        if max_price:
            obj = obj.filter(price__lte=int(min_price))
        if purpose:
            obj = obj.filter(purpose=int(purpose))
        if label:
            obj = obj.filter(label=label)
        if obj:
            obj = obj.order_by("-mark")[0]
            error = ''
        else:
            error = 'find nothing'

        return render(request, 'CPUNerd/match.html', {'obj': obj, 'error': error})


class CpuDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        obj = CpuModel.objects.get(id=int(kwargs['id']))
        last_obj = next_obj = None
        tem = CpuModel.objects.filter(id__lt=obj.id).values_list('id', 'description').order_by(
            "-id")
        if tem:
            last_obj = tem[0]
        tem = CpuModel.objects.filter(id__gt=obj.id).values_list('id', 'description').order_by(
            "id")
        if tem:
            next_obj = tem[0]
        return render(request, 'CPUNerd/cpu_detail.html', {'obj': obj, 'last_obj': last_obj, 'next_obj': next_obj})

    def post(self, request):
        pass


class RankView(LoginRequiredMixin, View):
    def get(self, request):
        cpu_obj_list = CpuModel.objects.all().order_by("-mark")
        return render(request, 'CPUNerd/rank.html', {'obj': cpu_obj_list})


class CommentView(LoginRequiredMixin, View):
    def post(self, request):
        cpu_id = request.GET.get("id")
        obj = CpuModel.objects.get(id=int(cpu_id))
        CommentModel.objects.create(user=request.user,cpu=obj,content=request.POST.get("remark", ""))
        return redirect(reverse('CPUNerd:cpu_detail', kwargs={'id': cpu_id}))


class CategoryView(LoginRequiredMixin, View):
    def get(self, request):
        category = int(request.GET.get("category"))
        cpu_obj_list = CpuModel.objects.filter(category=category)
        return render(request, 'CPUNerd/category.html',{'cpu_obj_list': cpu_obj_list})


class NewsView(LoginRequiredMixin, View):
    def get(self, request):
        obj_list = NewsModel.objects.all()
        return render(request, 'CPUNerd/news.html',{'obj_list': obj_list})


class NewsDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        obj = NewsModel.objects.get(id=int(kwargs['id']))
        return render(request, 'CPUNerd/news_detail.html', {'obj': obj})