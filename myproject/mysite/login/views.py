from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm


class IndexClass(View):
    def get(self, request):
        return HttpResponse('Hello')


class LoginClass(View):
    def get(self, request):
        return render(request, 'login/login.html')

    def post(self, request):
        user_name = request.POST.get('tendangnhap')
        password = request.POST.get('password')
        my_user = authenticate(username=user_name, password=password)
        if my_user is None:
            return HttpResponse('user khong ton tai %s %s' %(user_name, password))

        login(request, my_user)
        return render(request, 'login/thanhcong.html')


# class ViewUser(View):
#     def get(self, request):
#         if not request.user.is_authenticated:
#             return HttpResponse('ban vui long dang nhap')
#         else:
#             return HttpResponse('day la view-user')
#
#     def post(self, request):
#         pass


class ViewUser(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return HttpResponse('day la view-user')

    def post(self, request):
        pass


@decorators.login_required(login_url='/login/')
def view_product(request):
    return HttpResponse('xem san pham')


class AddPost(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        f = PostForm()
        context = {'fm': f}
        return render(request, 'login/add_post.html', context)

    def post(self, request):
        f = PostForm(request.POST)
        if not f.is_valid():
            return HttpResponse('ban nhap sai du lieu roi')

        #cache reload tu db user
        print(request.user.get_all_permissions())
        if request.user.has_perm('login.add_post'):
            f.save()
            return HttpResponse('add post thanh cong')
        else:
            return HttpResponse('may khong co quyen')