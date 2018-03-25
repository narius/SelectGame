# How the friendspart should work

# What the user do
User1 wants to befriend User2
- User1 clicks "Befriend" on User2's profile.
- A new FriendRequest is opened Sender=User1, Receiver=User2, status=Pending approval
- If User2 accepts the will both be added to each others Profile.friendlist.
- If User2 rejects the request FriendRequest.status=Rejected
