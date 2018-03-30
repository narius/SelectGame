from django.shortcuts import render
from django.shortcuts import HttpResponse
from Social.models import UserMessage
from Social.models import UserProfile
from Social.models import Notification
from SelectGame.models import Event
from django.utils.translation import gettext
from django.views import View
from django.contrib.auth.models import User


class EventView(View):
    '''
        Displays a specifik event.
    '''
    # TODO join button, only if there is room
    def get(self, request, event_id):
        user = request.user
        event = Event.objects.get(pk=event_id)
        profile = UserProfile.objects.get(user=user)
        friends = profile.friend_list.all()
        if not (user in event.participants.all() or user == event.owner):
            return HttpResponse(gettext("You are not part of this event"))
        return render(request,
                      'Social/view_event.html',
                      {'event': event,
                       'friends': friends})

    def post(self, request, event_id):
        user = request.user
        event = Event.objects.get(pk=event_id)
        if not (user in event.participants.all() or user == event.owner):
            return HttpResponse(gettext("You are not part of this event"))
        if request.POST.get("cancel"):
            return render(request,
                          'Social/view_event.html',
                          {'event': event, })
        if request.POST.get("new_message"):
            text = request.POST.get("message")
            new_message = UserMessage(writer=user, text=text)
            new_message.save()
            event.messages.add(new_message)
        if request.POST.get("invite_friends"):
            for pk in request.POST.getlist('friends'):
                invite = User.objects.get(pk=pk)
                notification = Notification(sender=user,
                                            receiver=invite)
                notification.save()
                event.notifications.add(notification)
                event.participants.add(invite)
            event.save()
        profile = UserProfile.objects.get(user=user)
        friends = profile.friend_list.all()
        return render(request,
                      'Social/view_event.html',
                      {'event': event,
                       'friends': friends})
