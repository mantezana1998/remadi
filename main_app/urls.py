from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='home'),
      path('about/', views.about, name='about'),
      path('dates/', views.dates_index, name='index'),
      path('list/', views.dates_list, name='list'),
      path('accounts/signup/', views.signup, name='signup'),
]