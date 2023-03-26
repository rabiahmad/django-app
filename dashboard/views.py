from django.shortcuts import render
from django.utils import timezone
# from models import Promotion, Transaction
from . import models
from django.http import HttpResponse
import pandas as pd
import plotly.express as px
from . import views
from django.template import RequestContext
from django.db.models import Sum



def index(request):
    return render(request, 'dashboard/index.html')
    
def promotions(request):
    promotions = models.Promotion.objects.all().order_by('start_date')
    return render(request, 'dashboard/promotions.html', {'promotions': promotions})

def transactions(request):
    transactions = models.Transaction.objects.all().order_by('order_date')
    return render(request, 'dashboard/transactions.html', {'transactions': transactions})

def overview(request):
    return render(request, 'dashboard/overview.html')

def total_sales(request):
    """ Get transactions data from database and calculate total sales"""
    # all_transactions = Transaction.objects.all()
    # transactions_data = [
    #     {
    #     'sales': t.sales,
    #     } for t in all_transactions 
    # ]
    # total_sales = sum([x['sales'] for x in transactions_data])

    total_sales = models.Transaction.objects.aggregate(Sum('price'))

    return render(request, 'dashboard/index.html', {'total_sales': total_sales})


    