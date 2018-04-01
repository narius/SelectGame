# Django imports
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

# SelectGame imports
from SelectGame.models import GameLibrary
from SelectGame.models import Game


class GameLibraryView(View):
    '''
        Displays and adds game to users gamlibrary
    '''

    def get(self, request, game_id=-1):
        user = request.user
        game_library = user.games
        games = Game.objects.all()
        return render(request,
                      'SelectGame/view_gamelibrary.html',
                      {'game_library': game_library,
                       'games': games
                      })

    def post(self, request, game_id=-1):
        user =  request.user
        # TODO add exception handler for game_id
        if game_id != -1:
            game = Game.objects.get(pk=game_id)
            user.games.games.add(game)
            user.games.save()
        games = Game.objects.all()
        return render(request,
                      'SelectGame/view_gamelibrary.html',
                      {'game_library': user.games,
                       'games': games
                      })
