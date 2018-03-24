from django.shortcuts import render
from django.shortcuts import HttpResponse
from Social.models import UserMessage
from SelectGame.models import Event
from django.utils.translation import gettext
from django.views import View


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
