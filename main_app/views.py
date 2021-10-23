from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return render(request, 'about.html')

def dates_index(request):
    return render(request, 'dates/index.html')
    # return render(request, 'dates/index.html', {'dates': dates})