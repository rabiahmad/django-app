from django.urls import path
from . import views

urlpatterns = [
    path('', views.promotions),
    path('promotions/', views.promotions, name='promotions'),
    path('transactions/', views.transactions, name='transactions'),
    path('dashboard/', views.dashboard, name='dashboard'),
]