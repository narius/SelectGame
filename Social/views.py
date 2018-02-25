from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from Social.models import model_user_profile
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the social index.")

def display_profile(request, user_id):
    user=User.objects.get(pk=user_id)
    users=User.objects.all()
    to_display_profile=True
    try:
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
