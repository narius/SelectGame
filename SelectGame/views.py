from django.http import HttpResponse
from django.shortcuts import render
from .models import model_rating
from .models import model_game
from .rating import rating_functions
from .models import model_location
from .models import model_event
from django.contrib.auth import logout
from django.core.signals import request_finished
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.signals import user_logged_in
from django.contrib import messages
from django.utils.translation import gettext
from .signals import *
from .forms import  add_game_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

@login_required(login_url='/login/')
def create_event(request):
    user=request.user
    #user=User.objects.get(pk=user_id)
    try:
        locations=model_location.objects.filter(owner=user)
    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, gettext('User has no locations'))
        locations={}
    if request.method=="POST":
        event_name=request.POST.get('event_name')
        location_id=request.POST.get('location_id')
        location=model_location.objects.get(pk=location_id)
        is_public=True if request.POST.get('is_public')=='on' else False
        event_date=request.POST.get('event_date')
        new_event=model_event.objects.create(name=event_name,
                            location=location,
                            owner=user,
                            is_public=is_public,
                            date=event_date)
        new_event.save()
        messages.add_message(request, messages.SUCCESS, gettext('Event created'))
    return render(request, 'SelectGame/create_event.html',{'locations':locations,
                                                            })

@login_required(login_url='/login/')
def all_events(request):
    events=model_event.objects.all()
    return render(request, 'SelectGame/all_events.html',{'events': events,})

@login_required(login_url='/login/')
def locations(request):
    user=request.user
    try:
        locations=model_location.objects.filter(owner=user)
    except ObjectDoesNotExist:
        locations={}
    return render(request, 'SelectGame/locations.html',{'locations':locations,})

def view_game(request, game_id):
    return render(request, 'SelectGame/view_game.html')
