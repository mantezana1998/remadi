from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.db.models.fields import CharField, DateField, TimeField
from django.contrib.auth.models import User
    
class Date(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=3000)
    cateogry = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    time = models.TimeField()
    dates = models.DateField()
    price = models.DecimalField(max_digits=400, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'date_id': self.id})

class Review(models.Model):
    decription = models.CharField(max_length=3000)
    dates = models.DateField()
    date = models.ForeignKey(Date, on_delete=models.CASCADE)

    def __str__(self):
        return self.name