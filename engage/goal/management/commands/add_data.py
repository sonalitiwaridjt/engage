import pandas as pd
import numpy as np

from goal.models import Movie, Genre, Keyword

from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    help = 'Add data to the database'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)

    def handle(self, *args, **options):
        file = None
        if options['file']:
            file = options['file']
        else:
            file = '..\data\movie_metadata_cleaned.csv'

        data = pd.read_csv(file)
        for _, r in data.iterrows():
            movieM = Movie()
            movieM.color = r['color']
            movieM.director_name = r['director_name']
            movieM.num_critic_for_reviews = r['num_critic_for_reviews']
            movieM.duration = r['duration']
            movieM.director_facebook_likes = r['director_facebook_likes']
            movieM.actor_3_facebook_likes = r['actor_3_facebook_likes']
            movieM.actor_2_name = r['actor_2_name']
            movieM.actor_1_facebook_likes = r['actor_1_facebook_likes']
            movieM.gross = r['gross']
            movieM.actor_1_name = r['actor_1_name']
            movieM.movie_title = ' '.join(r['movie_title'].split())
            movieM.num_voted_users = r['num_voted_users']
            movieM.cast_total_facebook_likes = r['cast_total_facebook_likes']
            movieM.actor_3_name = r['actor_3_name']
            movieM.facenumber_in_poster = r['facenumber_in_poster']
            movieM.movie_imdb_link = r['movie_imdb_link']
            movieM.num_user_for_reviews = r['num_user_for_reviews']
            movieM.language = r['language']
            movieM.country = r['country']
            movieM.content_rating = r['content_rating']
            movieM.budget = r['budget']
            movieM.title_year = r['title_year']
            movieM.actor_2_facebook_likes = r['actor_2_facebook_likes']
            movieM.imdb_score = r['imdb_score']
            movieM.aspect_ratio = r['aspect_ratio']
            movieM.movie_facebook_likes = r['movie_facebook_likes']
            movieM.popularity = r['popularity']
            movieM.save()

            for genre in r['genres'].split('|'):
                genreM = Genre.objects.get_or_create(name=genre)[0]
                movieM.genres.add(genreM)

            for keyword in r['plot_keywords'].split('|'):
                keywordM = Keyword.objects.get_or_create(name=keyword)[0]
                movieM.plot_keywords.add(keywordM)
