from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Date, MyDates
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from .apiaction import ticket_master_events, single_event

class DateDelete(DeleteView):
  model = MyDates
  success_url = '/categories/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def categories_dates_index(request):
  return render(request, 'dates/index.html')

def my_dates(request):
  ticketmaster_id = request.build_absolute_uri().split('=')[-1]
  event = single_event(ticketmaster_id)
  user = User.objects.get(username=request.user)
  print(event, '<------event')
  name = event['name']
  location = event['location']
  time = event['time']
  dates = event['dates']
  Date.objects.create(name=name, location=location, time=time, dates=dates, user_id=user.id)
  all_dates = Date.objects.filter(user=user)
  print(all_dates, '<------all dates!')
  return render(request, 'dates/my_dates.html', {
    'all_dates': all_dates
  })

def dates_lists(request):
  events = (ticket_master_events())
  dates = Date.objects.filter(user=request.user)
  print(request.user, events)
  return render(request, 'dates/dates_list.html', {'events' : events})

@login_required
def dates_detail(request, date_id):
  date = Date.objects.get(id=date_id)
  return render(request, 'dates/detail.html', {
    'date': date
    ['_embedded']['events']
  })  

@login_required
def assoc_dates(request, user_id, date_id):
  User.objects.get(id=user_id)
  return redirect('assoc_dates', user_id=user_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)