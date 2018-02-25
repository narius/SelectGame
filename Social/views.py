from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from Social.models import model_user_profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils.translation import gettext
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
    return render(request, 'Social/profile.html',{'to_display_profile':to_display_profile,'users':users,
                                                    'display_user':user,
                                                    'profile':profile,})
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
        return render(request, 'Social/profile.html',{  'to_display_profile':to_display_profile,
                                                        'users':users,
                                                        'display_user':user,
                                                        'profile':profile,})
    else:
        to_display_profile=False
        return render(request, 'Social/profile.html',{'to_display_profile':to_display_profile,'users':users,})

def edit_profile(request, user_id):
    # if this is a POST request we need to process the form data

    return render(request, 'Social/edit_profile.html', {})
