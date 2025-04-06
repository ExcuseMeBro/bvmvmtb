from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.db.models import Sum
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
from django.http import HttpResponse, JsonResponse
from .models import News, City

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
