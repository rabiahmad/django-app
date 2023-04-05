from django.urls import path
from dashboard import views
from dashboard.views import DashboardView

app_name = 'dashboard'

# URLConf
urlpatterns = [
    path('', DashboardView.as_view(), name='home'),
    path('tables/', views.tables, name='tables'),
    path('buttons/', views.buttons, name='buttons'),
    path('cards/', views.cards, name='cards'),
    path('transactions/', views.transactions, name='transactions'),
    path('overview/', views.overview, name='overview'),
]