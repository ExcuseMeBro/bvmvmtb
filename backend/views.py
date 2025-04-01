from django.shortcuts import render
from .models import *

def home(request):
    faqs = FAQ.objects.all()
    context = {'faqs': faqs}
    return render(request, 'index.html', context)


def murojaat(request):
    employee = Employee.objects.all()
    context = {'employees': employee}
    return render(request, 'murojaat.html', context)
