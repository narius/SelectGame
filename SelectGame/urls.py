from django.urls import path
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from . import views
app_name = 'selectgame'
urlpatterns = [
    path('', views.index, name='index'),
    path('ratings/',views.all_game_rating,name='all_game_rating'),
    path('login/', login, name='login'),
    path('add_game/', views.add_game, name='add_game'),
    path('create_event/', views.create_event, name='create_event'),
    path('all_events/', views.all_events, name='all_events'),
    path('locations/', views.locations, name='locations'),
    path('view_game/<int:game_id>/', views.view_game, name='view_game'),
    path('logout/', logout, {'next_page': 'selectgame:index'},name='logout'),
]
