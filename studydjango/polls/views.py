from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("欢迎你，你现在所在的是django的测试项目polls首页！！！");

def detail(request,question_id):
    return HttpResponse("You are looking at quetion %s."%question_id);

def results(request,question_id):
    response="You are looking at the results of question %s";
    return HttpResponse(response % question_id);

def vote(requst,question_id):
    return HttpResponse("You are voting on question %s." % question_id);
