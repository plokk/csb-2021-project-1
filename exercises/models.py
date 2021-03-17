from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Exercise(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()

class CreditCard(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.TextField()
    name = models.TextField()
    csv = models.TextField()
