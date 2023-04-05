from django.shortcuts import render
from dashboard.models import Transaction
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum, Count
from django.views.generic import TemplateView

import logging

from datetime import datetime, date
import pandas as pd
import calendar


class DashboardView(TemplateView):
    template_name = "dashboard/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_sales"] = self._total_sales()
        context["total_orders"] = self._total_orders()
        context["monthly_sales"] = self._monthly_sales_by_date()
        context["category_sales"] = self._sales_by_category()
        return context

    def _total_sales(self):
        """Get transactions data from database and calculate total sales"""
        total_sales_agg = Transaction.objects.aggregate(Sum("sales"))
        total_sales = "${:,}".format(int(total_sales_agg["sales__sum"]))
        return total_sales

    def _total_orders(self):
        """Get total number of orders from transactions dataset"""
        total_orders_agg = Transaction.objects.aggregate(Count("order_id"))
        total_orders = int(total_orders_agg["order_id__count"])
        return total_orders

    def _monthly_sales_by_date(self):
        """Get sum of sales by order date for chart"""
        labels = []
        data = []

        # data processing
        df = pd.DataFrame(list(Transaction.objects.all().values()))
        df["order_date"] = pd.to_datetime(df["order_date"])
        df["month_year"] = df["order_date"].dt.to_period("M")
        df = df.groupby("month_year").sum().reset_index()

        # returning the chart labels and data
        labels = list(df["month_year"].astype(str).values)
        data = list(df["sales"].values)
        context = {"labels": labels, "data": data}

        return context

    def _sales_by_category(self):
        """Get sales by category"""
        labels = []
        data = []

        df = pd.DataFrame(list(Transaction.objects.all().values()))
        df = df.groupby("category").sum().reset_index()

        labels = list(df["category"].values)
        data = list(df["sales"].values)

        context = {"labels": labels, "data": data}

        return context


def tables(request):
    return render(request, "dashboard/tables.html")


def buttons(request):
    return render(request, "dashboard/buttons.html")


def cards(request):
    return render(request, "dashboard/cards.html")


def transactions(request):
    transactions = Transaction.objects.all().order_by("order_date")
    return render(
        request, "dashboard/transactions.html", {"transactions": transactions}
    )


def overview(request):
    return render(request, "dashboard/overview.html")
