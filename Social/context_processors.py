from Social.models import Notification
from Social.models.Notification import NOTIFICATION_STATUS_UNREAD

def notifications_context_processor(request):
    user = request.user
    un_read_notifications = Notification.objects.filter(
                            receiver=user,
                            status=NOTIFICATION_STATUS_UNREAD
    ).count()
    has_unread = un_read_notifications > 0
    return {
        'has_unread': has_unread,
    }
