from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from Social.models import UserProfile
from Social.models import UserMessage
from Social.models import PrivateMessage
from SelectGame.models import GameLibrary
from SelectGame.models import Event
from SelectGame.rating import rating_functions
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils.translation import gettext
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views import View
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the social index.")


def display_profiles(request, user_id=-1):
    users = User.objects.all()
    if request.method == "POST":
        to_display_profile = True
        user_id = request.POST.get("user")
        print("user id: "+str(user_id))
        user = User.objects.get(pk=user_id)
    else:
        try:
            user = User.objects.get(pk=user_id) if int(user_id) > -1 else -1
        except ObjectDoesNotExist:
            user = {}
            messages.add_message(request,
                                 messages.ERROR,
                                 gettext('User doesn\'t exist'))
    try:
        to_display_profile = True
        profile = UserProfile.objects.get(user=user)
    except:
        to_display_profile = False
        profile = {}
    try:
        to_display_game_lbrary = True
        GameLibrary = GameLibrary.objects.get(owner=user)
        games = GameLibrary.games.all()
    except:
        to_display_game_lbrary=False
        GameLibrary = {}
        games = {}
    return render(request, 'Social/profile.html',
                  {'to_display_profile': to_display_profile,
                   'users': users,
                   'display_user': user,
                   'profile': profile,
                   'to_display_game_lbrary': to_display_game_lbrary,
                   'GameLibrary': GameLibrary,
                   'games': games,
                   'MEDIA_URL': settings.MEDIA_URL})


@login_required(login_url='/login/')
def edit_profile(request):
    # if this is a POST request we need to process the form data
    current_user = request.user
    print(request.POST.get("biography"))
    print(request.method)
    try:
        profile = UserProfile.objects.get(user=current_user)
        print(profile)
    except ObjectDoesNotExist:
        profile = UserProfile.objects.create(user=current_user)
    if request.method == "POST":
        new_profile_text = request.POST.get('biography')
        print(new_profile_text)
        profile.biography = new_profile_text
        profile.save()
    return render(request, 'Social/edit_profile.html', {'profile': profile, })


@login_required(login_url='/login')
def view_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    user = request.user
    user_is_allowed = user in event.participants.all()\
        or user == event.owner\
        or event.is_public
    if not user_is_allowed:
        messages.add_message(request,
                             messages.ERROR,
                             gettext('You are not allowed to see this event'))
        return render(request, 'SelectGame/index.html')
    if request.method == 'POST':
        message = UserMessage(writer=user, text=request.POST.get('message'))
        message.save()
        event.messages.add(message)
    users = []
    users.append(event.owner)
    for participant in event.participants.all():
        users.append(participant)
    average = rating_functions.users_rating(users, 2)
    return render(request, 'Social/view_event.html', {'event': event,
                                                      'averages': average})


class PrivateMessageView(View):
    '''
        View to display private messages
    '''
    def get(self, request, message_id=None):
        user = request.user
        print(message_id)
        if message_id is None:
            # Get all PrivateMessages where user user is a participants
            private_messages = PrivateMessage.objects.all()#.\
                #filter(participants__in=[user, ])
            print("private_messages")
            print(private_messages)
            return render(request, 'Social/view_privatemessages.html', {
                "private_messages": private_messages,
                })
        # Get the PrivateMessge with pk=message_id,
        # and check if user is participant
        private_message = PrivateMessage.objects.get(pk=message_id)
        if user in private_message.participants:
            return render(request, 'Social/view_privatemessage.html', {
                "private_message": private_message,
                })
        else:
            messages.add_message(request,
                                 messages.ERROR,
                                 gettext('You are not part of this conversation'))
            private_messages = PrivateMessage.objects.all().\
                filter(participants__in=[user, ])
            return render(request, 'Social/view_privatemessages.html', {
                "private_messages": private_messages,
                })
