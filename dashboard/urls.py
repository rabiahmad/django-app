from django.urls import path
from . import views

urlpatterns = [
    path('', views.promo_list, name='promo_list'),
]