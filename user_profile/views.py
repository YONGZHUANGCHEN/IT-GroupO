import json
from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, login, logout
from user_profile.models import UserProfile
from django.db.models import Q
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile

# Create your views here.

# 自定义权限认证
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

# 登录模块
class LoginRequiredMixin(object):
    """
    登陆限定，并指定登陆url
    """
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='/user-profile/login/')


# 注册模块
class RegisterView(View):
    def get(self, request):
        return render(request, 'user_profile/register.html')

    def post(self, request):
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        rePassword = request.POST.get('rePassword')
        if password != rePassword:
            return render(request, 'user_profile/register.html', {'error': '两次密码输入不一致'})

        user = UserProfile.objects.filter(Q(username=username) | Q(email=email))
        if user:   # 已存在邮箱或者账号
            return render(request, 'user_profile/register.html', {'error': '邮箱或者账号已存在'})

        obj = UserProfile.objects.create(username=username, first_name=firstname,last_name=lastname, email=email)
        obj.set_password(password)
        obj.save()
        return HttpResponseRedirect(reverse('user_profile:login'))

# 退出模块
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('user_profile:login'))

# 登录模块
class LoginView(View):
    def get(self, request):
        return render(request, 'user_profile/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_remember_me = request.POST.get('is_remember_me')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session.set_expiry(0)
                if is_remember_me:
                    request.session.set_expiry(None)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "user_profile/login.html", {"error": "用户未激活！"})
        else:
            return render(request, "user_profile/login.html", {"error": "用户名或密码错误！"})

# 用户信息模块
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user_id = request.GET.get("user_id")
        if not user_id:
            return render(request, 'user_profile/profile.html', {"user": request.user, 'myself': True})
        else:
            try:
                obj = UserProfile.objects.get(id=int(user_id))
            except Exception as e:
                return render(request, 'user_profile/error.html', {"error": "用户不存在"})
            if obj.id == int(user_id):
                return render(request, 'user_profile/profile.html', {"user": obj, 'myself': True})
            return render(request, 'user_profile/profile.html', {"user": obj, 'myself': False})

    def post(self, request):
        user_id = request.POST.get("id")
        last_name = request.POST.get("name")
        interest = request.POST.get("interest")
        sex = request.POST.get("sex")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        obj = UserProfile.objects.get(id=int(user_id))
        obj.last_name = last_name
        obj.interest = interest
        obj.sex = int(sex)
        obj.address = address
        obj.phone = phone
        obj.email = email
        obj.save()
        return HttpResponseRedirect(reverse("profile") + "?id=" + user_id)


# 修改头像模块
class ChangeAvatarView(LoginRequiredMixin, View):

    def post(self, request):
        obj = UserProfile.objects.get(id=request.user.id)
        pic = ContentFile(request.FILES['file'].read())
        obj.image.save(request.FILES['file'].name, pic)
        obj.save()
        return HttpResponse(json.dumps({'code':0, "avatar": obj.image.url}))

# 重置密码
class ResetPasswordView(LoginRequiredMixin, View):
    def post(self, request):
        obj = UserProfile.objects.get(id=request.user.id)
        password = request.POST.get("password")
        obj.set_password(password)
        obj.save()
        return HttpResponse(json.dumps({'code':0, "avatar": obj.image.url}), content_type="application/json")
