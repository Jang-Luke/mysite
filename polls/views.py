from django.http import HttpResponse
from django.template import loader

from .models import Question, Choice

def polls(request):
    lastest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "lastest_question_list": lastest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question {0}.".format(question_id))

def results(request, question_id):
    response = "You're looking at the results of question {0}."
    return HttpResponse(response.format(question_id))

def vote(request, question_id):
    return HttpResponse("You're voting on question {0}".format(question_id))