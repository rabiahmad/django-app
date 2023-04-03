from django.shortcuts import render
from django.utils import timezone
from dashboard.models import Promotion, Transaction
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum, Count
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_sales"] = self._total_sales()
        context["total_orders"] = self._total_orders()
        return context

    def _total_sales(self):
        """ Get transactions data from database and calculate total sales """
        total_sales_agg = Transaction.objects.aggregate(Sum("sales"))
        total_sales = "${:,}".format(int(total_sales_agg["sales__sum"]))
        return total_sales
    
    def _total_orders(self):
        """ Get total number of orders from transactions dataset """
        total_orders_agg = Transaction.objects.aggregate(Count("order_id"))
        total_orders = int(total_orders_agg["order_id__count"])
        return total_orders
    

def tables(request):
    return render(request, "dashboard/tables.html")


def buttons(request):
    return render(request, "dashboard/buttons.html")


def cards(request):
    return render(request, "dashboard/cards.html")


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
