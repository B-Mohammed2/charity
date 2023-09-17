from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('account_login/', auth_views.LoginView.as_view(), name='login'),
    # path('account/signup/', auth_views.SignupView.as_view(), name='account_signup'),
    # path('account/login/', auth_views.LoginView.as_view(), name='account_login'), 
]

