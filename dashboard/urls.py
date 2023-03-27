from django.urls import path
from dashboard import views

app_name = 'dashboard'

# URLConf
urlpatterns = [
    path('', views.index, name='dashboard'),
    path('', views.total_sales, name='total_sales'),
    path('promotions/', views.promotions, name='promotions'),
    path('transactions/', views.transactions, name='transactions'),
    path('overview/', views.overview, name='overview'),
]