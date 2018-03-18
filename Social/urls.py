from django.urls import path
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from . import views
app_name = 'social'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:user_id>/', views.display_profiles, name='user_profile'),
    path('profile/', views.display_profiles, name='profiles'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('event/<int:event_id>/', views.view_event, name='view_event'),
    path('view_friends/', login_required(views.view_friends.as_view()), name='view_friends'),
    path('find_friends/', login_required(views.find_friends.as_view()), name='find_friends'),
]
