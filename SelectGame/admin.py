from django.contrib import admin
from  .models import model_category, model_game, model_location,model_rating
# Register your models here.
admin.site.register(model_category)
admin.site.register(model_game)
admin.site.register(model_location)
admin.site.register(model_rating)
