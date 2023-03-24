from django.shortcuts import render

def promo_list(request):
    return render(request, 'dashboard/promo_list.html', {})
