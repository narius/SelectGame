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
from .signals import *
from .forms import  add_game_form
def index(request):
    return render(request, 'SelectGame/index.html')

def all_game_rating(request):
    ratings=model_rating.objects.all()
    games=model_game.objects.all()
    mean_rating_per_game=rating_functions.mean_rating_per_game(games)
    for mean_r in mean_rating_per_game:
        print(type(mean_r))
    return render(request, 'SelectGame/all_game_rating.html',{'ratings':mean_rating_per_game,})

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request,'registration/logged_out.html')

def add_game(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = add_game_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            h=1
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
    # if a GET (or any other method) we'll create a blank form
    form=add_game_form()
    return render(request, 'SelectGame/add_game.html',{'form':form})
