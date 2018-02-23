from django.urls import path

from . import views
app_name = 'selectgame'
urlpatterns = [
    path('', views.index, name='index'),
    path('ratings/',views.all_game_rating,name='all_game_rating'),
]
