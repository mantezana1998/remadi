from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dates_index(request):
  return render(request, 'dates/index.html')
  # return render(request, 'dates/index.html', {'dates': dates})

def dates_list(request):
  return render(request, 'dates/lists.html')

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