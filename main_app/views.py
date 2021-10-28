from django.shortcuts import render, redirect
from .models import Date, MyDates
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .apiaction import ticket_master_events

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def categories_dates_index(request):
  # dates = Date.objects.filter(user=request.user)
  return render(request, 'dates/index.html')

def my_dates(request):
  return render (request, 'dates/my_dates.html')

def dates_lists(request):
  events = (ticket_master_events())
  print(events)
  return render(request, 'dates/dates_list.html', {'events' : events})



@login_required
def dates_detail(request, date_id):
  date = Date.objects.get(id=date_id)
  # print(request, '<-this is my request')
  # print(date_id, '<- this is my date')
  # print('_embedded', 'events', '<- THIS IS OUR EVENTS')
  return render(request, 'dates/detail.html', {
    'date': date
    ['_embedded']['events']
  })  

def assoc_dates(request, user_id, date_id):
  MyDates.objects.get(id=user_id).dates.add(user_id)
  return redirect('assoc_dates', user_id=user_id)

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