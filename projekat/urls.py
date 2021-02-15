from django.urls import path
from . import views

app_name = 'projekat'

urlpatterns = [
    path('', views.userPage, name='userPage'),
    path('user', views.user, name='userPage')
]