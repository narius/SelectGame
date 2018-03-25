from django.shortcuts import render
from django.shortcuts import HttpResponse
from Social.models import UserProfile
from Social.models import FriendRequest
from django.utils.translation import gettext
from django.views import View


class FriendsView(View):
    '''
        Displays friend list.
    '''
    def get(self, request):
        user = request.user
        [profile, created] = UserProfile.objects.get_or_create(user=user)
        friends = profile.friend_list.all() if not created else None
        sent_request = FriendRequest.objects.all().\
                                     filter(sender=user).\
                                     exclude(status="AC")
        received_request = FriendRequest.objects.all().\
                                     filter(receiver=user).\
                                     exclude(status="AC")
        return render(request,
                      'Social/friends.html',
                      {'profile': profile,
                       'sent': sent_request,
                       'received': received_request})

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
