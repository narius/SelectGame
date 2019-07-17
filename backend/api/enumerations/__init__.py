class FEATURE_FLAGS(enumerate):
    NEED_REGISTRATION_CODE = True


class FRIEND_STATUS(enumerate):
    SENT = 'friendship.status.sent'
    REJECTED = 'friendship.status.rejected'
    ACCEPTED = 'friendship.status.accepted'


class EVENT_INVITE_STATUS(enumerate):
    SENT = 'event.status.sent'
    REJECTED = 'event.status.rejected'
    ACCEPTED = 'event.status.accepted'
