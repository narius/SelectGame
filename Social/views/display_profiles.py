from django.shortcuts import render
from django.contrib.auth.models import User
from Social.models import UserProfile
from SelectGame.models import GameLibrary
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils.translation import gettext
from django.conf import settings


def display_profiles(request, user_id=-1):
    users = User.objects.all()
    game_library = {}
    if request.method == "POST":
        to_display_profile = True
        user_id = request.POST.get("user")
        print("user id: "+str(user_id))
        user = User.objects.get(pk=user_id)
    else:
        try:
            user = User.objects.get(pk=user_id) if int(user_id) > -1 else -1
        except ObjectDoesNotExist:
            user = {}
            messages.add_message(request,
                                 messages.ERROR,
                                 gettext('User doesn\'t exist'))
    try:
        to_display_profile = True
        profile = UserProfile.objects.get(user=user)
    except:
        to_display_profile = False
        profile = {}
    try:
        to_display_game_lbrary = True
        game_library = GameLibrary.objects.get(owner=user)
        games = game_library.games.all()
    except:
        to_display_game_lbrary = False
        GameLibrary = {}
        games = {}
    return render(request, 'Social/profile.html',
                  {'to_display_profile': to_display_profile,
                   'users': users,
                   'display_user': user,
                   'profile': profile,
                   'to_display_game_lbrary': to_display_game_lbrary,
                   'GameLibrary': GameLibrary,
                   'games': games,
                   'MEDIA_URL': settings.MEDIA_URL})
