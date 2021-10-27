from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# CATEGORIES = (
#     ('AD', 'Affordable Dates'),
#     ('SO', 'Special Occasions'),
#     ('AV', 'Adventurous Dates')
# )

class Date(models.Model):
    user = models.ManyToManyField(User)
    # category = models.CharField(
    #     max_length=2,
    #     choices=CATEGORIES,
    #     default=CATEGORIES[0][0]
    # )

    # def __str__(self):
    #     return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'date_id': self.id})

class MyDates(models.Model):
    date_id = models.ForeignKey(Date, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)