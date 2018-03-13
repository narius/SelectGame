from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from Social.models import model_user_profile
from Social.models import model_message
from Social.models import model_friend_list
from Social.models import FRIENDS_STATUS
from SelectGame.models import model_game_library
from SelectGame.models import model_event
from SelectGame.rating import rating_functions
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils.translation import gettext
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the social index.")

def display_profiles(request, user_id=-1):
    users=User.objects.all()
    if request.method=="POST":
        to_display_profile=True
        user_id=request.POST.get("user")
        print("user id: "+str(user_id))
        user=User.objects.get(pk=user_id)
    else:
        try:
            user=User.objects.get(pk=user_id) if int(user_id)>-1 else -1
        except ObjectDoesNotExist:
            user={}
            messages.add_message(request, messages.ERROR, gettext('User doesn\'t exist'))
    try:
        to_display_profile=True
        profile=model_user_profile.objects.get(user=user)
    except:
        to_display_profile=False
        profile={}
    try:
        to_display_game_lbrary=True
        game_library=model_game_library.objects.get(owner=user)
        games=game_library.games.all()
    except:
        to_display_game_lbrary=False
        game_library={}
        games={}
    return render(request, 'Social/profile.html',{  'to_display_profile':to_display_profile,
                                                        'users':users,
                                                        'display_user':user,
                                                        'profile':profile,
                                                        'to_display_game_lbrary':to_display_game_lbrary,
                                                        'game_library':game_library,
                                                        'games': games,
                                                        'MEDIA_URL':settings.MEDIA_URL})

@login_required(login_url='/login/')
def edit_profile(request):
    # if this is a POST request we need to process the form data
    current_user = request.user
    print(request.POST.get("biography"))
    print(request.method)
    try:
        profile=model_user_profile.objects.get(user=current_user)
        print(profile)
    except ObjectDoesNotExist:
        profile=model_user_profile.objects.create(user=current_user)
    if request.method=="POST":
        new_profile_text=request.POST.get('biography')
        print(new_profile_text)
        profile.biography=new_profile_text
        profile.save()
    return render(request, 'Social/edit_profile.html', {'profile':profile,})


@login_required(login_url='/login')
def view_event(request, event_id):
    event = model_event.objects.get(pk=event_id)
    user = request.user
    user_is_allowed = user in event.participants.all()\
                    or user == event.owner\
                    or event.is_public
    if not user_is_allowed:
        messages.add_message(request, messages.ERROR, gettext('You are not allowed to see this event'))
        return render(request, 'SelectGame/index.html')
    if request.method=='POST':
        message=model_message(writer=user, text=request.POST.get('message'))
        message.save()
        event.messages.add(message)
    users=[]
    users.append(event.owner)
    for participant in event.participants.all():
        users.append(participant)
    average=rating_functions.users_rating(users, 2)
    return render(request, 'Social/view_event.html', {'event': event,
                                                    'averages': average})


@login_required(login_url='/login')
def view_friends(request):
    user = request.user
    friend_list = model_friend_list.objects.get_or_create(user=user)[0]
    accepted = []
    pending = []
    rejected = []
    removed = []
    friends_pending = 'pe'
    friends_accepted = 'ac'
    friends_rejected = 're'
    friends_removed = 'rm'
    for friend in friend_list.friends.all():
        if friend.status == friends_pending:
            pending.append(friend)
        if friend.status == friends_accepted:
                accepted.append(friend)
        if friend.status == friends_rejected:
            rejected.append(friend)
        if friend.status == friends_removed:
            removed.append(friend)
    return render(request, 'Social/view_friends.html', {'accepted': accepted,
                                                        'pending': pending,
                                                        'rejected': rejected,
                                                        'removed': removed})
