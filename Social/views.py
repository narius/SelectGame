from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from Social.models import model_user_profile
from Social.models import model_message
from Social.models import model_friends, model_relationsship
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
from django.views import View
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



class view_friends(View):
    def get(self, request, *args, **kwargs):
        '''
            If a user sends a friend request user_from will be the user,
            user_from.status will be approved and user_to.status will be pending.
            returns
                pending: request that the one I seent to need to approved
                waiting_approval: requests sent to me, that i need approved
                accepted: request that both users have Accepted
                rejected: requests that user_to has rejected
                removed: requests that user_from has withdrawed.
        '''
        user = request.user
        print(user)
        my_statuses = model_relationsship.objects.all().filter(user=user)
        friends=[]
        for status in my_statuses:
            friends.append(model_friends.objects.all().filter(Q(user_to=status)|Q(user_from=status)))
        accepted = []
        pending = []
        rejected = []
        removed = []
        waiting_approval = []
        friends_pending = 'pe'
        friends_accepted = 'ac'
        friends_rejected = 're'
        friends_removed = 'rm'
        for friend in friends:
            #Check if the user i user_from or user_to
            my_friend = friend[0].user_to if friend[0].user_from.user == user else friend[0].user_from
            if friend[0].user_from.status == friends_accepted and friend[0].user_to.status == friends_accepted:
                accepted.append(my_friend)
            if friend[0].user_from.user == user and my_friend.status == friends_pending:
                pending.append(my_friend)
            #If I haven't approved the friend request
            if friend[0].user_to.user == user and friend[0].user_to.status == friends_pending:
                waiting_approval.append(my_friend)
        return render(request, 'Social/view_friends.html', {'accepted': accepted,
                                                            'pending': pending,
                                                            'rejected': rejected,
                                                            'removed': removed,
                                                            'waiting_approval': waiting_approval})
