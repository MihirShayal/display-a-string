from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('<marquee><h1>It is my First View<h1><marquee>')
