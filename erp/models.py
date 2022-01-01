from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    STATUS = (
        ('before', 'Przed naprawą'),
        ('in_progress', 'W trakcie naprawy'),
        ('after', 'Po naprawie'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=15,
        choices=STATUS,
        default='before',
    )
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
