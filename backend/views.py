from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, world!")
