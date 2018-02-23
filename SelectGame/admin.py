from django.contrib import admin
from  .models import model_category, model_event
from .models import model_game, model_location,model_rating
from .models import model_game_library
# Register your models here.
admin.site.register(model_category)
admin.site.register(model_game)
admin.site.register(model_location)
admin.site.register(model_rating)
admin.site.register(model_event)
admin.site.register(model_game_library)
