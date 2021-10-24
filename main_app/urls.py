from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='home'),
      path('about/', views.about, name='about'),
      path('dates/', views.dates_index, name='index'),
      path('lists/', views.dates_list, name='lists'),
      path('accounts/signup/', views.signup, name='signup'),
      path('dates/<int:date_id>/', views.dates_detail, name='detail'),
]