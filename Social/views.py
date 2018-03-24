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


class EventView(View):
    '''
        Displays a specifik event.
    '''
    def get(self, request, event_id):
        user = request.user
        event = Event.objects.get(pk=event_id)
        if not (user in event.participants.all() or user == event.owner):
            return HttpResponse(gettext("You are not part of this event"))
        return render(request,
                      'Social/view_event.html',
                      {'event': event, })

    def post(self, request, event_id):
        user = request.user
        event = Event.objects.get(pk=event_id)
        if not (user in event.participants.all() or user == event.owner):
            return HttpResponse(gettext("You are not part of this event"))
        if request.POST.get("cancel"):
            return render(request,
                          'Social/view_event.html',
                          {'event': event, })
        text = request.POST.get("message")
        new_message = UserMessage(writer=user, text=text)
        new_message.save()
        event.messages.add(new_message)
        return render(request,
                      'Social/view_event.html',
                      {'event': event, })


class PrivateMessageView(View):
    '''
        View to display private messages
    '''
    def get(self, request):
        user = request.user
        # Get all PrivateMessages where user user is a participants
        private_messages = PrivateMessage.objects.all().\
            filter(participants__in=[user, ])
        print("private_messages")
        print(private_messages)
        return render(request, 'Social/view_privatemessages.html', {
            "private_messages": private_messages,
            })

    def post(self, request):
        user = request.user
        private_messages = PrivateMessage.objects.all().\
            filter(participants__in=[user, ])
        for private_message in private_messages:
            if request.POST.get("new_message_"+str(private_message.id)):
                text = request.POST.get("new_message_text_"
                                        + str(private_message.id))
                new_message = UserMessage(writer=user, text=text)
                new_message.save()
                private_message.messages.add(new_message)
        return render(request, 'Social/view_privatemessages.html', {
            "private_messages": private_messages,
            })
