from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    username = "Rabi"
    render(request, 'mysite/index.html', {'name': username})
