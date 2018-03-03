from django.test import TestCase
from SelectGame.models import model_rating
from SelectGame.models import model_game
from django.contrib.auth.models import User
from .rating import rating_functions
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.signals import user_logged_in
from django.db.models import signals

#Test for the rating functions
class RatingTestCase(TestCase):
    def setUp(self):
        print("Hi from RatingTestCase")
        user_logged_in.disconnect()
        self.game=model_game.objects.create(name="TestGame1")
        self.games=model_game.objects.all()
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        self.user2 = User.objects.create_user(username='testuser2', password='12345')
        login = self.client.login(username='testuser2', password='12345')
        model_rating.objects.create(game=self.game, user=self.user,rating=4)
        model_rating.objects.create(game=self.game, user=self.user2,rating=5)

    def test_rating_per_game(self):
        self.assertEqual(rating_functions.mean_rating_per_game(self.games), [{'game':self.game,
                                                                                'mean_rating':4.5,
                                                                                'votes':2}])
