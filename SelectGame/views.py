from django.http import HttpResponse
from django.shortcuts import render
from .models import model_rating
from .models import model_game
from .rating import rating_functions
def index(request):
    return render(request, 'SelectGame/index.html')

def all_game_rating(request):
    ratings=model_rating.objects.all()
    games=model_game.objects.all()
    mean_rating_per_game=rating_functions.mean_rating_per_game(games)
    print(type(mean_rating_per_game))
    print(ratings)
    for mean_r in mean_rating_per_game:
        print(mean_r)
    return render(request, 'SelectGame/all_game_rating.html',{'ratings':mean_rating_per_game,})
