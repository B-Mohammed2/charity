from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('charities/', views.all_organizations, name='charities'),
 
]
