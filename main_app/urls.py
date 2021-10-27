from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='home'),
      path('about/', views.about, name='about'),
      path('my_dates/', views.my_dates, name='my_dates'),
      path('accounts/signup/', views.signup, name='signup'),
      path('categories/', views.categories_dates_index, name='index'),
      path('categories/dates/', views.dates_lists, name='lists'),
      path('categories/dates/<int:date_id>', views.dates_detail, name='detail'),
      path('categories/dates/<int:date_id>/my_dates', views.assoc_dates, name='assoc_dates'),
]