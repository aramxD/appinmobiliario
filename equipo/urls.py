from django.contrib import admin
from django.urls import  path
from .views import *

#Reiniciar contrasenia
from django.contrib.auth import views as auth_views

urlpatterns = [    
    
    #Registro y autentificacion
    path('registro/', registro, name='registro'),
    path('login/', loginuser, name='loginuser'),
    path('logout/', logoutuser, name='logoutuser'),

    #Reiniciar contrasena
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset_password_form.html"), name='password_reset_confirm'),
    path('reset_password_complete_=D/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_done.html"), name='password_reset_complete'),


]