from django.db import models
from django.db.models.fields import DateField, FloatField, TimeField, CharField
from django.db.models.fields.files import ImageField
from django.urls import reverse
from django.contrib.auth.models import User

class Date(models.Model):
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    time = models.TimeField('Time of Event')
    dates = models.DateField('Day of Event')
    price = models.DecimalField(max_digits=500, decimal_places=2)
    image = models.ImageField()
    user = models.ManyToManyField(User)
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'date_id': self.id})

class MyDates(models.Model):
    date_id = models.ForeignKey(Date, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)