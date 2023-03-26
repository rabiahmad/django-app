from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.index, name='home'),
    path('promotions/', views.promotions, name='promotions'),
    path('transactions/', views.transactions, name='transactions'),
    path('overview/', views.overview, name='overview'),
    path('total_sales/', views.total_sales, name='total_sales')
]