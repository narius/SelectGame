from django.shortcuts import render
from SelectGame.models import Rating
from SelectGame.models import Game
from SelectGame.rating import rating_functions


def view_game(request, game_id):
    game = Game.objects.get(pk=game_id)
    user_rating = Rating.objects.get_or_create(game=game, user=request.user)[0]
    if request.method == 'POST':
        if request.POST.get("1-star"):
            user_rating.rating = 1
        if request.POST.get("2-star"):
            user_rating.rating = 2
        if request.POST.get("3-star"):
            user_rating.rating = 3
        if request.POST.get("4-star"):
            user_rating.rating = 4
        if request.POST.get("5-star"):
            user_rating.rating = 5
        user_rating.save()
    # Sets the color of the stars
    stars = ['btn btn-default btn-grey btn-sm',
             'btn btn-default btn-grey btn-sm',
             'btn btn-default btn-grey btn-sm',
             'btn btn-default btn-grey btn-sm',
             'btn btn-default btn-grey btn-sm']
    if user_rating.rating >= 1:
        stars = ['btn btn-warning btn-sm',
                 'btn btn-default btn-grey btn-sm',
                 'btn btn-default btn-grey btn-sm',
                 'btn btn-default btn-grey btn-sm',
                 'btn btn-default btn-grey btn-sm']
    if user_rating.rating >= 2:
        stars = ['btn btn-warning btn-sm',
                 'btn btn-warning btn-sm',
                 'btn btn-default btn-grey btn-sm',
                 'btn btn-default btn-grey btn-sm',
                 'btn btn-default btn-grey btn-sm']
    if user_rating.rating >= 3:
        stars = ['btn btn-warning btn-sm',
                 'btn btn-warning btn-sm',
                 'btn btn-warning btn-sm',
                 'btn btn-default btn-grey btn-sm',
                 'btn btn-default btn-grey btn-sm']
    if user_rating.rating >= 4:
        stars = ['btn btn-warning btn-sm',
                 'btn btn-warning btn-sm',
                 'btn btn-warning btn-sm',
                 'btn btn-warning btn-sm',
                 'btn btn-default btn-grey btn-sm']
    if user_rating.rating >= 5:
        stars = ['btn btn-warning btn-sm',
                 'btn btn-warning btn-sm',
                 'btn btn-warning btn-sm',
                 'btn btn-warning btn-sm',
                 'btn btn-warning btn-sm']
    mean_rating = rating_functions.mean_rating_per_game([game, ])
    return render(request,
                  'SelectGame/view_game.html',
                  {'game': game,
                   'user_rating': user_rating,
                   'rating': mean_rating[0],
                   'stars': stars})
