from django.shortcuts import render
from dashboard.models import Transaction
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum, Count
from django.views.generic import TemplateView


def login_user(request):
    return render(request, "registration/login.html")


def register_user(request):
    return render(request, "registration/register.html")