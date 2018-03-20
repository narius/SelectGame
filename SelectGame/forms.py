from django import forms
from django.forms import ModelForm
from SelectGame.models import Game, Category


class add_game_form(ModelForm):
    name = forms.CharField(max_length=100)
    category = forms.ModelMultipleChoiceField(
                queryset=Category.objects.all())
    # image = forms.ImageField(required=False)
    comment = forms.CharField(required=False)
    minimum_number_of_players = forms.IntegerField()
    maximum_number_of_players = forms.IntegerField()

    class Meta:
        model = Game
        fields = ['name', 'category']
        fields = ['name',
                  'category',
                  # 'image',
                  'comment',
                  'maximum_number_of_players',
                  'minimum_number_of_players']
