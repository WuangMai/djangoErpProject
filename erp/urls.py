from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='erp-home'),
    path('logowanie/', views.login, name='erp-login'),
    path('rejestracja/', views.register, name='erp-register')
]
