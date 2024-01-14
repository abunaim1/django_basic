from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse("THIS IS COURSES PAGE")

def about(request):
    return HttpResponse("I am from about")

def home(request):
    return HttpResponse("I am from HOME")