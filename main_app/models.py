from django.db import models
from django.urls import reverse
from django.db.models.fields import CharField, DateField, TimeField
from django.contrib.auth.models import User

CATEGORIES = (
    ('AD', 'Affordable Dates'),
    ('SO', 'Special Occasions'),
    ('AV', 'Adventurous Dates')
)

class Date(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=3000)
    location = models.CharField(max_length=250)
    time = models.TimeField('Time of Event')
    dates = models.DateField('Date of Event')
    price = models.DecimalField(max_digits=400, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=2,
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
    )

    def __str__(self):
        return f"{self.get_category_display()}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'date_id': self.id})

class Review(models.Model):
    description = models.CharField(max_length=3000)
    dates = models.DateField('Date of Review')
    date = models.ForeignKey(Date, on_delete=models.CASCADE)

    def __str__(self):
        return self.name