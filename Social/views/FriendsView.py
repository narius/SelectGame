from django.shortcuts import render
from django.shortcuts import HttpResponse
from Social.models import UserProfile
from Social.models import FriendRequest
from django.utils.translation import gettext
from django.views import View
from django.db.models import Q

class FriendsView(View):
    '''
        Displays friend list.
    '''
    def get(self, request):
        user = request.user
        [profile, created] = UserProfile.objects.get_or_create(user=user)
        friends = profile.friend_list.all() if not created else None
        sent_filter = Q(sender=user)&Q(status="PE")
        sent_request = FriendRequest.objects.all().\
                                     filter(sent_filter)
        print("Sent")
        print(sent_request)
        rec_filter = Q(status="PE") & Q(receiver=user)
        received_request = FriendRequest.objects.all().\
                                     filter(rec_filter)
        filter = Q(status="RE") & (Q(sender=user) | Q(receiver=user))
        rejected = FriendRequest.objects.all().\
                                     filter(filter)

        return render(request,
                      'Social/friends.html',
                      {'profile': profile,
                       'friends': friends,
                       'sent': sent_request,
                       'received': received_request,
                       'rejected': rejected})

    def post(self, request):
        user = request.user
        filter = Q(sender=user)|Q(receiver=user)
        friend_request = FriendRequest.objects.all().filter(filter)
        print("post")
        for friend in friend_request:
            print(friend.id)
            print(request.POST.get("Accept_"+str(friend.id)))
            print("Accept_"+str(friend.id))
            if request.POST.get("Accept_"+str(friend.id)):
                print("Accept")
                friend.status = "AC"
                friend.save()
            if request.POST.get("Reject_"+str(friend.id)):
                friend.status = "RE"
                friend.save()
        [profile, created] = UserProfile.objects.get_or_create(user=user)
        friends = profile.friend_list.all() if not created else None
        sent_filter = Q(sender=user) & ~Q(status="AC")
        sent_request = FriendRequest.objects.all().\
                                     filter(sent_filter)
        print("Sent")
        print(sent_request)
        received_request = FriendRequest.objects.all().\
                                     filter(receiver=user).\
                                     exclude(status="AC")
        return render(request,
                      'Social/friends.html',
                      {'profile': profile,
                       'friends': friends,
                       'sent': sent_request,
                       'received': received_request})
