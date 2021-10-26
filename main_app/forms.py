from django.forms import ModelForm
from .models import Date

class AddDate(ModelForm):
    class Meta: 
        model = Date
        fields = '__all__'