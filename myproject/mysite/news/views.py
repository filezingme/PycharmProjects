from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendMail
from .models import Post as News
from django.views import View

# Create your views here.

# def index(request):
#     return HttpResponse("hello")


class IndexClass(View):
    def get(self, request):
        return HttpResponse("hello world")

# def viewlist(request):
#     list_question = News.objects.all()
#     context = {"newslist": list_question}
#     return render(request, "news/news_list.html", context)


class ListClass(View):
    def get(self, request):
        list_question = News.objects.all()
        context = {"newslist": list_question}
        return render(request, "news/news_list.html", context)

# def add_post(request):
#     a = PostForm()
#     return render(request, 'news/add_news.html', {'f': a})

# class AddClass(View):
#     def get(self, request):
#         a = PostForm()
#         return render(request, 'news/add_news.html', {'f': a})

# def save_news(request):
#     if request.method == "POST":
#         g = PostForm(request.POST)
#         if g.is_valid():
#             g.save()
#             return HttpResponse("save success")
#         else:
#             return HttpResponse("invalid")
#     else:
#         return HttpResponse("it is not post request")


class ClassSaveNews(View):
    def get(self, request):
        a = PostForm()
        return render(request, 'news/add_news.html', {'f': a})

    def post(self, request):
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("save success")
        else:
            return HttpResponse("invalid")


def email_view(request):
    b = SendMail()
    return render(request, 'news/email.html', {'f': b})


def process(request):
    if request.method == "POST":
        m = SendMail(request.POST)
        if m.is_valid():
            title = m.cleaned_data['title']
            cc = m.cleaned_data['cc']
            content = m.cleaned_data['content']
            email = m.cleaned_data['email']

            context = {'title':title, 'cc':cc, 'content':content, 'email':email}

            context2 = {'email_data':m}

            return render(request, 'news/print_email.html', context2)
        else:
            return HttpResponse("form is not validate")
    else:
        return HttpResponse('form is not Post method')
