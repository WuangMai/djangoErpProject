from django.shortcuts import render
from .models import Order


def login(request):
    context = {
        'orders': Order.objects.all()
    }
    return render(request, 'erp/login.html', context)


def register(request):
    return render(request, 'erp/register.html', {'title': 'Rejestracja'})


def home(request):
    return render(request, 'erp/home.html')
