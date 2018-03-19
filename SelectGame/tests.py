from django.test import TestCase
from SelectGame.models import Rating
from SelectGame.models import Game
from SelectGame.models import  GameLibrary
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
        self.game=Game.objects.create(name="TestGame1")
        self.games=Game.objects.all()
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        login = self.client.login(username='testuser1', password='12345')
        self.user2 = User.objects.create_user(username='testuser2', password='12345')
        login = self.client.login(username='testuser2', password='12345')
        Rating.objects.create(game=self.game, user=self.user1,rating=4)
        Rating.objects.create(game=self.game, user=self.user2,rating=5)
        self. GameLibrary1= GameLibrary.objects.create(owner=self.user1)
        self. GameLibrary1.games.add(self.game)
        self. GameLibrary2= GameLibrary.objects.create(owner=self.user2)
        self. GameLibrary2.games.add(self.game)
    def test_rating_per_game(self):
        self.assertEqual(rating_functions.mean_rating_per_game(self.games), [{'game': self.game,
                                                                'mean_rating': 4.5,
                                                                'total': 2,
                                                                'votes': [0, 0, 0, 1, 1],
                                                                'width': [0, 0, 0, 50, 50]}])

    def test_users_rating(self):
        users = [self.user1, self.user2]
        lower_limit = 2
        self.assertEqual(rating_functions.users_rating(users, lower_limit), [{'avarage': 4.5,
  'game': self.game,
  'number_of_votes': {'TestGame1': 2}}])
