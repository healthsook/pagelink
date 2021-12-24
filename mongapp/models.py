from django.conf import settings
from django.db import models
from django.utils import timezone
from accounts.models import Users

# Create your models here.

class Record(models.Model):
    pub_date = models.DateField(auto_now_add=True)
    cal = models.CharField(max_length=1000)
    walk = models.CharField(max_length=10000)
    hour = models.CharField(max_length=100)
    min = models.CharField(max_length=100)

    def __str__(self):
        return self.pub_date

class Mongs(models.Model):
    monguser = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, verbose_name="현유저")
