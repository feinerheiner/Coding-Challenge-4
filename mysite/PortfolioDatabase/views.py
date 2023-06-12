from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby
from .models import Project


# Create your views here.
def Home(request):
    return HttpResponse('Welcome to my Portfolio. My name is Richard Heiner. I have an Associates Degree in General'
                        'Studies and in Computer Science. I am working on my Bachelers Degree in Computer Science.'
                        'So far I have enjoyed programming in multiple languages, including: Python, Java, Javascript,'
                        'and C++.')


def Hobbies(request):
    hobby_list = Hobby.objects.all()
    return HttpResponse( hobby_list)


def Portfolio(request):
    project_list = Project.objects.all()
    return HttpResponse(project_list)


def Contact(request):
    return HttpResponse('Here is my email address: feinerheiner91@gmail.com')


