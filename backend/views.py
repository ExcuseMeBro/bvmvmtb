from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from .models import *

def home(request):
    votes = Vote.objects.all()
    total_votes = votes.aggregate(total=Sum('count'))['total'] or 0
    
    for vote in votes:
        vote.percentage = (vote.count / total_votes * 100) if total_votes > 0 else 0
    
    context = {
        'votes': votes,
    }

    if request.method == 'POST':
        try:
            offer = Offer(
                fullname=request.POST.get('fullname'),
                region_id=request.POST.get('region'),
                city_id=request.POST.get('city'),
                phone=request.POST.get('phone'),
                category=request.POST.get('category'),
                message=request.POST.get('message')
            )
            offer.save()
            messages.success(request, _('Taklifingiz muvaffaqiyatli yuborildi'))
            return redirect('home')
        except Exception as e:
            messages.error(request, _('Xatolik yuz berdi. Iltimos qayta urinib ko\'ring'))
    
    faqs = FAQ.objects.all()
    statistics = Statistics.objects.all()
    links = UsefulLink.objects.all()
    news_items = News.objects.all().order_by('-created_at')[:8]
    regions = Region.objects.all()
    offerStats = OfferStats.objects.all()
    context.update({
        'faqs': faqs,
        'statistics': statistics,
        'links': links,
        'news_items': news_items,
        'regions': regions,
        'offerStats': offerStats,
    })
    return render(request, 'index.html', context)


def persons(request, cat_id):
    person_type = PersonType.objects.filter(id=cat_id).first()
    persons = Persons.objects.filter(type=person_type)
    if person_type:
        context = {
            'id': person_type.id,
            'name': person_type.name,
            'name_uz': person_type.name_uz,
            'name_ru': person_type.name_ru
        }
    else:
        context = None
    return render(request, 'persons.html', {'person_type': context, 'persons': persons})

def purpose(request):
    return render(request, 'purpose.html')

def terms(request):
    return render(request, 'terms.html')

def school(request):
    return render(request, 'school.html')

def recruitment(request):
    return render(request, 'recruitment.html')

def egov(request):
    return render(request, 'egov.html')

def open(request):
    return render(request, 'open.html')

def ijro(request):
    return render(request, 'ijro.html')

def investment(request):
    return render(request, 'investment.html')

def employees(request):
    employee = Employee.objects.all()

    context = {
        'employees': employee,
    }

    return render(request, 'employees.html', context)

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
from django.http import JsonResponse
from .models import News, City, Persons

def person_detail(request, pk):
    person = get_object_or_404(Persons, pk=pk)
    return render(request, 'person_detail.html', {'person': person})


def get_cities(request, region_id):
    cities = City.objects.filter(region_id=region_id).values()
    return JsonResponse(list(cities), safe=False)

def get_leaders(request, region_id):
    try:
        leaders = Leader.objects.filter(region_id=region_id).values()
        
        all_leaders = list(leaders)
        return JsonResponse(all_leaders, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_city_leader(request, city_id):
    try:
        leader = DistrictLeader.objects.filter(city_id=city_id).first()
        if leader:
            leader_data = {
                'id': leader.id,
                'name': leader.fullname,
                'phone': leader.phone,
                'address': leader.address,
                'latitude': leader.location_latitude,
                'longitude': leader.location_longitude,
            }
            return JsonResponse(leader_data)
        return JsonResponse({'error': 'Leader not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def news_list(request):
    news_items = News.objects.all().order_by('-created_at')
    return render(request, 'news_list.html', {'news_items': news_items})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news_single.html', {'news': news})

def about(request):
    about = get_object_or_404(About.objects.order_by('-created_at'))
    return render(request, 'about.html', {'about': about})

def vote(request):
    if request.method == 'POST':
        try:
            vote_option = request.POST.get('vote')
            vote_obj, created = Vote.objects.get_or_create(option=vote_option)
            vote_obj.count += 1
            vote_obj.save()
            messages.success(request, _('Ovozingiz muvaffaqiyatli qabul qilindi'))
        except Exception as e:
            messages.error(request, _('Xatolik yuz berdi. Iltimos qayta urinib ko\'ring'))
    return redirect('home')
