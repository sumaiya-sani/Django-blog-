
from re import template
from unicodedata import name
from django import views
from django.urls import path
from.views import *
from django.contrib.auth import views as auth_views

app_name="members"

urlpatterns = [
    path('register/',UserRegisterForm.as_view(),name="register"),
    path('edit_profile/',UserEditView.as_view(),name="edit_profile"),
    path('/password/',auth_views.PasswordChangeView.as_view(template_name='change_password.html')),
    path('<int:pk>/profile/',UserProfileView.as_view(),name="members_profile"),
    path('login/',views.login_page,name='login'),

  #path('/password/',PasswordsChangeView.as_view(template_name='change_password.html'))

    
]
