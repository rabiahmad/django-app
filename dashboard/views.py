from django.shortcuts import render
from django.utils import timezone
from .models import Promotion, Transaction


def promotions(request):
    promotions = Promotion.objects.all().order_by('start_date')
    return render(request, 'dashboard/promotions.html', {'promotions': promotions})

def transactions(request):
    transactions = Transaction.objects.all().order_by('order_date')
    return render(request, 'dashboard/transactions.html', {'transactions': transactions})

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
