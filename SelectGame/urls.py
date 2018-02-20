from django.urls import path

from . import views
app_name = 'selectgame'
urlpatterns = [
    path('', views.index, name='index'),
]
