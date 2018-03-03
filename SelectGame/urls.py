from django.urls import path
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from . import views
app_name = 'selectgame'
urlpatterns = [
    path('', views.index, name='index'),
    path('ratings/',views.all_game_rating,name='all_game_rating'),
    path('login/', login, name='login'),
    path('add_game', views.add_game, name='add_game'),
    path('logout/', logout, {'next_page': 'selectgame:index'},name='logout'),
]
