from django.shortcuts import render
from SelectGame.models import Rating
from SelectGame.models import Game
from .rating import rating_functions
from SelectGame.models import Location
from SelectGame.models import Event
from SelectGame.models import Category
from django.contrib.auth import logout
from django.contrib import messages
from django.utils.translation import gettext
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return render(request, 'SelectGame/index.html')


def test_acc(request):
    return render(request, 'SelectGame/test_acc.html')


def all_game_rating(request):
    games = Game.objects.all()
    mean_rating_per_game = rating_functions.mean_rating_per_game(games)
    return render(request,
                  'SelectGame/all_game_rating.html',
                  {'ratings': mean_rating_per_game, })


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'registration/logged_out.html')


def add_game(request):
    if request.method == 'POST':
        print(request.FILES['image'])
        data = {'name': request.POST.get('name'),
                'category': request.POST.get('category'),
                'comment': request.POST.get('comment'),
                'image': request.FILES['image'],
                'minimum_number_of_players':
                request.POST.get('minimum_number_of_players'),
                'maximum_number_of_players':
                request.POST.get('maximum_number_of_players')
                }
        new_game = Game(name=data['name'],
                        comment=data['comment'],
                        image=data['image'],
                        minimum_number_of_players=data[
                        'minimum_number_of_players'],
                        maximum_number_of_players=data[
                        'maximum_number_of_players'])
        new_game.save()
        for pk in request.POST.getlist('category'):
            category = Category.objects.get(pk=pk)
            new_game.category.add(category)
        new_game.save()
    categories = Category.objects.all()
    return render(request,
                  'SelectGame/add_game.html',
                  {'categories': categories})


@login_required(login_url='/login/')
def create_event(request):
    '''

            **Return dictionary**

            * locations: all the locations that the current user own.

            **Template:**

            :template:`SelectGame/create_event.html`
    '''
    user = request.user
    # user=User.objects.get(pk=user_id)
    try:
        locations = Location.objects.filter(owner=user)
    except ObjectDoesNotExist:
        messages.add_message(request,
                             messages.ERROR,
                             gettext('User has no locations'))
        locations = {}
    if request.method == "POST":
        event_name = request.POST.get('event_name')
        location_id = request.POST.get('location_id')
        location = Location.objects.get(pk=location_id)
        is_public = True if request.POST.get('is_public') == 'on' else False
        event_date = request.POST.get('event_date')
        new_event = Event.objects.create(name=event_name,
                                         location=location,
                                         owner=user,
                                         is_public=is_public,
                                         date=event_date)
        new_event.save()
        messages.add_message(request,
                             messages.SUCCESS,
                             gettext('Event created'))
    return render(request,
                  'SelectGame/create_event.html',
                  {'locations': locations, })


@login_required(login_url='/login/')
def all_events(request):
    events = Event.objects.all()
    return render(request, 'SelectGame/all_events.html', {'events': events, })


@login_required(login_url='/login/')
def locations(request):
    user = request.user
    try:
        locations = Location.objects.filter(owner=user)
    except ObjectDoesNotExist:
        locations = {}
    return render(request,
                  'SelectGame/locations.html',
                  {'locations': locations, })


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
