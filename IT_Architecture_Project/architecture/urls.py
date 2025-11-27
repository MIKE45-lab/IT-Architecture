from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students/', views.students, name='students'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout')
]