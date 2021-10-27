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

    def get_absolute_url(self):
        return reverse('detail', kwargs={'date_id': self.id})