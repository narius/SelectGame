from django.shortcuts import render
from Social.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


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
