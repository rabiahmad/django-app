from django.urls import path
from dashboard import views

app_name = 'dashboard'

# URLConf
urlpatterns = [
    path('', views.index, name='index'),
    path('tables/', views.tables, name='tables'),
    path('buttons/', views.buttons, name='buttons'),
    path('cards/', views.cards, name='cards'),
    path('total_sales/', views.total_sales, name='total_sales'),
    path('promotions/', views.promotions, name='promotions'),
    path('transactions/', views.transactions, name='transactions'),
    path('overview/', views.overview, name='overview'),
]