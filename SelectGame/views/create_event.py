from django.shortcuts import render
from SelectGame.models import Location
from SelectGame.models import Event
from django.contrib import messages
from django.utils.translation import gettext
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


@login_required(login_url='/login/')
def create_event(request):
    '''

            **Return dictionary**

            * locations: all the locations that the current user own.

            **Template:**

            :template:`SelectGame/create_event.html`
    '''
    user = request.user
    # user=User.objects.get(pk=user_id)
    try:
        locations = Location.objects.filter(owner=user)
    except ObjectDoesNotExist:
        messages.add_message(request,
                             messages.ERROR,
                             gettext('User has no locations'))
        locations = {}
    if request.method == "POST":
        event_name = request.POST.get('event_name')
        location_id = request.POST.get('location_id')
        location = Location.objects.get(pk=location_id)
        is_public = True if request.POST.get('is_public') == 'on' else False
        event_date = request.POST.get('event_date')
        new_event = Event.objects.create(name=event_name,
                                         location=location,
                                         owner=user,
                                         is_public=is_public,
                                         date=event_date)
        new_event.save()
        messages.add_message(request,
                             messages.SUCCESS,
                             gettext('Event created'))
    return render(request,
                  'SelectGame/create_event.html',
                  {'locations': locations, })
