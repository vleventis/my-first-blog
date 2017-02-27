from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    credits = models.IntegerField(default=0)

class Call(models.Model):
    country_name = models.CharField(max_length=30)
    rate = models.FloatField(default=1)
    duration = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, models.SET_NULL, blank= True, null= True,)
    target_no = models.CharField(max_length=12, blank= True)
    timeofcall = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return self.country_name






