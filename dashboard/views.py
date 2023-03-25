from django.shortcuts import render
from django.utils import timezone
from .models import Promotion


def promo_list(request):
    promos = Promotion.objects.all().order_by('start_date')
    return render(request, 'dashboard/promo_list.html', {'promos': promos})
