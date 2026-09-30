from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'dashboard'

urlpatterns = [
   path( '', views.Index , name="index" ),
   path( 'create-subject/', views.CreateSubject, name='create_subject')
]
