from django.contrib import admin
from .models import model_user_profile
from .models import model_group
from .models import model_message
from .models import model_group_message
from .models import model_friend_list
from .models import model_private_message
from .models import model_relationsship
# Register your models here.
admin.site.register(model_user_profile)
admin.site.register(model_group)
admin.site.register(model_message)
admin.site.register(model_group_message)
admin.site.register(model_friend_list)
admin.site.register(model_private_message)
admin.site.register(model_relationsship)
