from django.db import models
from django.db.models.fields import DateField, FloatField, TimeField, CharField
from django.db.models.fields.files import ImageField
from django.urls import reverse
from django.contrib.auth.models import User

class Date(models.Model):
    name = models.CharField(max_length=500, null=True)
    location = models.CharField(max_length=100, null=True)
    time = models.TimeField('Time of Event', null=True)
    dates = models.DateField(null=True, default=None)
    price = models.DecimalField(max_digits=500, decimal_places=2, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'date_id': self.id})

class MyDates(models.Model):
    date_id = models.ForeignKey(Date, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)