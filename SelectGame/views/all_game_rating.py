from django.shortcuts import render
from SelectGame.models import Game
from .rating import rating_functions


def all_game_rating(request):
    games = Game.objects.all()
    mean_rating_per_game = rating_functions.mean_rating_per_game(games)
    return render(request,
                  'SelectGame/all_game_rating.html',
                  {'ratings': mean_rating_per_game, })
