from django.shortcuts import render
from django.utils import timezone
from dashboard.models import Promotion, Transaction
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum


def index(request):
    return render(request, "dashboard/index.html")


def promotions(request):
    promotions = Promotion.objects.all().order_by("start_date")
    return render(request, "dashboard/promotions.html", {"promotions": promotions})


def transactions(request):
    transactions = Transaction.objects.all().order_by("order_date")
    return render(
        request, "dashboard/transactions.html", {"transactions": transactions}
    )


def overview(request):
    return render(request, "dashboard/overview.html")


def total_sales(request):
    """Get transactions data from database and calculate total sales"""
    total_sales_agg = Transaction.objects.aggregate(Sum("sales"))
    total_sales = "${:,}".format(int(total_sales_agg["sales__sum"]))
    context = {"total_sales": total_sales}
    return render(request, "dashboard/index.html", context)
