# pylint: disable=E1101
from Social.models import Notification
from Social.models.Notification import NOTIFICATION_STATUS_UNREAD

def notifications_context_processor(request):
    print("notifications_context_processor")
    # We can't get notifications if user is not logged in
    if request.user.is_authenticated():
        return
    user = request.user

    # Gets the last 10 notifications
    notifications = Notification.objects.filter(
                            receiver=user,
    )[:10]
    # TODO: Get links for events, messages, groups etc from notifcation
    for notification in notifications:
        print("Message")
        print(len(notification.message.all()))
        print("Group")
        print(len(notification.group.all()))
    un_read_notifications = Notification.objects.filter(
                            receiver=user,
                            status=NOTIFICATION_STATUS_UNREAD
    ).count()
    has_unread = un_read_notifications > 0
    return {
        'has_unread': has_unread,
        'notifications': notifications
    }
