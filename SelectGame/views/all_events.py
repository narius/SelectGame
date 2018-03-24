from django.shortcuts import render
from SelectGame.models import Event
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def all_events(request):
    events = Event.objects.all()
    return render(request, 'SelectGame/all_events.html', {'events': events, })
