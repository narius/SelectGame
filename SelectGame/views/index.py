from django.shortcuts import render

# SelectGame imports
from SelectGame.models import GameLibrary

# Social imports
from Social.models import UserProfile


def index(request):
    if request.user.is_anonymous:
        return render(request,
                      'SelectGame/index-anonymous.html',
                      {})
    user = request.user
    game_library = GameLibrary.objects.get_or_create(owner=user)[0]
    profile = user.profile
    return render(request,
                  'SelectGame/index.html',
                  {'game_library': game_library,
                   'profile': profile})
