from django.shortcuts import render
from SelectGame.models import Location
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


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
