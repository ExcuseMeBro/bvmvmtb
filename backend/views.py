from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from .models import *

def home(request):
    faqs = FAQ.objects.all()
    statistics = Statistics.objects.all()
    links = UsefulLink.objects.all()
    news_items = News.objects.all().order_by('-created_at')[:8]
    context = {
        'faqs': faqs,
        'statistics': statistics,
        'links': links,
        'news_items': news_items
        }
    return render(request, 'index.html', context)


def murojaat(request):
    if request.method == 'POST':
        try:
            email_form = EmailForm(
                subject=request.POST.get('subject'),
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                father_name=request.POST.get('father_name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                region_id=request.POST.get('region'),
                message=request.POST.get('message')
            )
            if 'attachment' in request.FILES:
                email_form.attachment = request.FILES['attachment']
            email_form.save()
            messages.success(request, _('Murojaat muvaffaqiyatli yuborildi'))
            return redirect('murojaat')
        except Exception as e:
            messages.error(request, _('Xatolik yuz berdi. Iltimos qayta urinib ko\'ring'))
    
    employee = Employee.objects.all()
    regions = Region.objects.all()
    context = {
        'employees': employee,
        'regions': regions,
    }
    return render(request, 'murojaat.html', context)

from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request):
    news_items = News.objects.all().order_by('-created_at')
    return render(request, 'news_list.html', {'news_items': news_items})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news_single.html', {'news': news})
