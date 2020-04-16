from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import question
# Create your views here.
def index(request):
    latest_question = question.objects.order_by('-pub_date')[:5]
    context = {'latest_question': latest_question}
    return render(request, 'templates/home.html', context)

def detail(request,question_id):
    quest =get_object_or_404(question, pk=question_id)
    return render(request, 'templates/detail.html', {'question':quest})

def results(request,question_id):
    return HttpResponse("You're looking at the result of question: %s" % question_id)
def vote(request,question_id):
    return HttpResponse("You're are voting on question: %s " % question_id)