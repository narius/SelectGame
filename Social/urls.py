from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from SelectGame.views import index
app_name = 'social'
urlpatterns = [
    path('', index, name='index'),
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
         login_required(views.EventView.as_view()),
         name='view_event'),
    path('messages/',
         login_required(views.PrivateMessageView.as_view()),
         name='view_messages'),
    path('notifications/',
         login_required(views.NotificationView.as_view()),
         name='notifications'),
    path('friends/',
         login_required(views.FriendsView.as_view()),
         name='friends'),
]
