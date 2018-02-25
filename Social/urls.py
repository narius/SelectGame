from django.urls import path
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from . import views
app_name = 'social'
urlpatterns = [
    path('', views.index, name='index'),
]
