from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Choice

# Create your views here.

def index(request):
    name = "thang"
    taisan = ['xe may', 'dien thoai']
    context = {"name": name, "taisan": taisan}
    return render(request, "polls/index.html", context)

def viewlist(request):
    list_question = Question.objects.all()
    context = {"dsquest": list_question}
    return render(request, "polls/question_list.html", context)

def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html", {"qs": q})

def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        data = request.POST["choice"]
        c = q.choice_set.get(pk=data)
        c.vote = c.vote + 1
        c.save()
    except:
        HttpResponse("loi khong co choice")
    return render(request, "polls/result.html", {"q": q})