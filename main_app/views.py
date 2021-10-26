from django.shortcuts import render, redirect
from .models import Date, Review
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .forms import DateForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def dates_index(request):
  dates = Date.objects.filter(user=request.user)
  return render(request, 'dates/index.html', {'dates': dates})

def my_dates(request):
  return render (request, 'dates/my_dates.html')

@login_required
def dates_detail(request, date_id):
  date = Date.objects.get(id=date_id)
  return render(request, 'dates/detail.html', {
    'date': date
  })  

def add_date(request, date_id):
  form = DateForm(request.POST)
  if form.is_valid():
    new_date = form.save(commit=False)
    new_date.date_id = date_id
    new_date.save()
  return redirect('my_dates', date_id=date_id)

class DateCreate(CreateView):
  model = Date
  fields = '__all__'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)