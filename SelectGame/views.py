from django.http import HttpResponse
from django.shortcuts import render
from .models import model_rating
from .models import model_game
from .rating import rating_functions
from django.contrib.auth import logout
from django.core.signals import request_finished
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.signals import user_logged_in
from django.contrib import messages
from django.utils.translation import gettext
@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    messages.add_message(request, messages.SUCCESS, gettext('Logged in.'))

@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(request, messages.SUCCESS, gettext('Logged out.'))



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

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request,'registration/logged_out.html')
