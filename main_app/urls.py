from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='home'),
      path('about/', views.about, name='about'),
      path('my_dates/', views.my_dates, name='my_dates'),
      path('accounts/signup/', views.signup, name='signup'),
      path('categories/', views.categories_dates_index, name='index'),
      # can not run the same function at different urls 'dates_detail'
      # rename the function from dates_detail to date_list 
      path('categories/dates/', views.dates_detail, name='detail'),
      # catrgory/dates will display a list of dates query from the api 
      # For when our API is set, uncomment this ^^^
      # This path will display a details page for a individual date
      path('categories/dates/<int:date_id>/', views.dates_detail, name='detail'),
]