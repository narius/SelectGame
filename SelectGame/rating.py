# a file for function around ratings

from .models import Rating
from .models import GameLibrary
from SelectGame.models import EventGame


class rating_functions():
    # Function to calulate the average for games
    def mean_rating_per_game(games):
        mean_rating_per_game = []
        for game in games:
            ratings = Rating.objects.filter(game=game).values('rating')
            total = len(ratings)
            votes = [0, 0, 0, 0, 0]
            width = [0, 0, 0, 0, 0]
            if (total != 0):
                for rating in ratings:
                    votes[rating['rating']-1] = votes[rating['rating']-1]+1
                n = 0
                while n < 5:
                    width[n] = int(round((votes[n]/total)*100))
                    n = n+1
                mean_rating = sum(rating['rating']
                                  for rating in ratings) / total
            else:
                mean_rating = 0
            mean_rating_per_game.append({'game': game,
                                         'mean_rating': mean_rating,
                                         'total': total,
                                         'votes': votes,
                                         'width': width})
        return mean_rating_per_game

    def event_users_rating(event, users, lower_limit):
        """
            This function will return the average rating for all games that
            :model:`auth.User` have
            rated higher than lower_limit
        """

        games = []
        ratings = {}
        number_of_votes = {}
        avarage = []
        voters = []
        for user in users:
            # Retrieve all games that the users own.
            voters.append(user.user)
            users_game_library = \
                GameLibrary.objects.get_or_create(owner=user.user)[0]
            for i in users_game_library.games.all():
                games.append(i)
        for game in games:
            print(game)
            user_ratings = \
                Rating.objects.all().filter(user__in=voters).filter(game=game)
            print(str(user)+" - "+str(game))
            for rating in user_ratings:
                if rating.rating > lower_limit:
                    ratings[rating.game.name] = \
                        ratings.setdefault(rating.game.name, 0)\
                        + rating.rating
                    number_of_votes[rating.game.name] = \
                        number_of_votes.setdefault(rating.game.name, 0)+1
            if game not in games:
                print("rating-append: "+str(game))
                games.append(game)
        # By now whe should have two list, one with all available game,
        # one with all ratings.
        for game in games:
            # Find all ratings for this game
            game_avarage = ratings.setdefault(game.name, 0) \
                           / number_of_votes.setdefault(game.name, 1)
            votes = number_of_votes[game.name]
            too_low = True if game_avarage == 0 else False
            new_event_game = EventGame.objects.get_or_create(event=event,
                                                            game=game)[0]
            new_event_game.average = game_avarage
            new_event_game.number_of_rated = votes
            new_event_game.too_low = too_low
            new_event_game.save()
        return new_event_game
