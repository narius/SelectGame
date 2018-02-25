from django.urls import path
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from . import views
app_name = 'social'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:user_id>/', views.display_profile, name='user_profile'),
    path('profile/', views.display_profiles, name='profiles')
]
