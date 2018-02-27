from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from Social.models import model_user_profile
from SelectGame.models import model_game_library
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils.translation import gettext
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the social index.")

def display_profile(request, user_id):
    try:
        to_display_profile=True
        user=User.objects.get(pk=user_id)
    except ObjectDoesNotExist:
        user={}
        messages.add_message(request, messages.ERROR, gettext("User doesn't exist."))
        to_display_profile=False
    users=User.objects.all()
    try:
        profile={}
        if user!={}:
            to_display_profile=True
            profile=model_user_profile.objects.get(user=user)
    except ObjectDoesNotExist:
        profile={}
    try:
        to_display_game_lbrary=True
        game_library=model_game_library.objects.get(owner=user)
        games=game_library.games.all()
    except ObjectDoesNotExist:
        to_display_game_lbrary=False
        game_library={}
        games={}
    return render(request, 'Social/profile.html',{'to_display_profile':to_display_profile,'users':users,
                                                    'display_user':user,
                                                    'profile':profile,
                                                    'to_display_game_lbrary':to_display_game_lbrary,
                                                    'game_library':game_library,
                                                    'games': games})

def display_profiles(request):
    users=User.objects.all()
    if request.method=="POST":
        to_display_profile=True
        user_id=request.POST.get("user")
        print("user id: "+str(user_id))
        user=User.objects.get(pk=user_id)
        try:
            profile=model_user_profile.objects.get(user=user)
        except ObjectDoesNotExist:
            profile={}
        try:
            to_display_game_lbrary=True
            game_library=model_game_library.objects.get(owner=user)
            games=game_library.games.all()
        except ObjectDoesNotExist:
            to_display_game_lbrary=False
            game_library={}
            games={}
        return render(request, 'Social/profile.html',{  'to_display_profile':to_display_profile,
                                                        'users':users,
                                                        'display_user':user,
                                                        'profile':profile,
                                                        'to_display_game_lbrary':to_display_game_lbrary,
                                                        'game_library':game_library,
                                                        'games': games})
    else:
        to_display_profile=False
        return render(request, 'Social/profile.html',{'to_display_profile':to_display_profile,'users':users,})

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
