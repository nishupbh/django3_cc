from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def News(request):
    return HttpResponse("<h1>This is latest news </h1>")


def Home(request):
    return HttpResponse("<h1>This is our home page </h1>")


def Contact(request):
    return HttpResponse("<h1>This is our contact page </h1>")
