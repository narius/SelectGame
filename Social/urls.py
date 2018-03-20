from django.urls import path

from . import views
app_name = 'social'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:user_id>/',
         views.display_profiles,
         name='user_profile'),
    path('profile/',
         views.display_profiles,
         name='profiles'),
    path('edit_profile/',
         views.edit_profile,
         name='edit_profile'),
    path('event/<int:event_id>/',
         views.view_event,
         name='view_event')
]
