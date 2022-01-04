from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from erp import models


@login_required
def status(request):
    context = {
        'orders': models.Order.objects.filter(client_id=request.user.id)
    }
    return render(request, 'users/status.html', context)
