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
    profile=model_user_profile.objects.get(user=user)
    return render(request, 'Social/profile.html',{'user':user,
                                                    'profile':profile,})
def display_profiles(request):
    users=User.objects.all()
    if request.method=="POST":
        user_id=request.POST.get("user")
        print("user id: "+str(user_id))
        user=User.objects.get(pk=user_id)
        try:
            profile=model_user_profile.objects.get(user=user)
        except ObjectDoesNotExist:
            profile={}
        return render(request, 'Social/profile.html',{'users':users,
                                                        'user':user,
                                                        'profile':profile,})
    else:
        return render(request, 'Social/profile.html',{'users':users,})
