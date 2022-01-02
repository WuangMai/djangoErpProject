from django.contrib import admin
from .models import Order

list_display = ('name', 'status', 'date_added',)
admin.site.register(Order)
