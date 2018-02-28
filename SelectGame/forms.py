from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext
from SelectGame.models import model_game, model_category

class add_game_form(ModelForm):
    name = forms.CharField(max_length=100)
    category = forms.ModelMultipleChoiceField(queryset=model_category.objects.all())
    class Meta:
        model=model_game
        fields=['name','category']
