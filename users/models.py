from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

import erp.models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    date_added = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# class Status(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     orderList = models.ManyToOneRel(user, erp.models.Order, field_name='client', on_delete=models.DO_NOTHING)
