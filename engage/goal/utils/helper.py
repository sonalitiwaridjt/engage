from django.contrib.gis.geoip2 import GeoIP2
import pickle
from mlxtend.preprocessing import TransactionEncoder
from ..models import Movie

import pandas as pd


def get_allowed_ratings(age):
    content_rating = ['Approved', 'G', 'GP', 'PG', 'PG-13',
                      'Unrated', 'Not Rated', 'Passed', 'R', 'X', 'NC-17', 'M']

    if age >= 18:
        return content_rating
    elif age >= 17:
        return content_rating[:-1]
    elif age >= 16:
        return content_rating[:-3]
    elif age >= 15:
        return content_rating[:-4]
    elif age >= 14:
        return content_rating[:-6]
    elif age >= 13:
        return content_rating[:5]
    elif age >= 10:
        return content_rating[:4]
    elif age >= 7:
        return content_rating[:3]
    elif age >= 2:
        return content_rating[:2]
    elif age >= 0:
        return content_rating[:1]
    else:
        return []


def add_new_movie(q):
    data = pd.DataFrame(
        [{'id': x.id, 'movie_title': x.movie_title, 'genres': '|'.join([i.name for i in x.genres.all()],)} for x in q])
    x = data['genres'].str.split('|')
    te = TransactionEncoder()
    x = te.fit_transform(x)
    x = pd.DataFrame(x, columns=te.columns_)
    genres = x.astype('int')
    genres.insert(0, 'movie_title', data['movie_title'])
    genres = genres.set_index('movie_title')
    genres.to_pickle('static\pkl\genres.pkl')


def get_transformed_data(file='static\pkl\genres.pkl'):
    with open(file, 'rb') as f:
        data = pickle.load(f)
    return data


def get_last_count(file='static\last_count.txt'):
    with open(file, 'r') as f:
        last_count = f.read()
    return int(last_count)


def set_last_count(count, file='static\last_count.txt'):
    with open(file, 'w') as f:
        f.write(str(count))


def getGenres(mood):
    genres = []
    if mood == 'neutral':
        genres = ['Animation', 'Biography',
                  'Documentary', 'History', 'Western']
    elif mood == 'happy':
        genres = ['Action', 'Adventure', 'Comedy',
                  'Fantasy', 'Family', 'Romance', 'Sci-Fi']
    elif mood == 'sad':
        genres = ['Music', 'Musical', 'Mystery', 'Romance']
    elif mood == 'angry':
        genres = ['Action', 'Crime', 'Drama', 'Horror', 'Thriller']
    elif mood == 'fearful':
        genres = ['Sport', 'Mystery', 'Thriller']
    elif mood == 'disgusted':
        genres = ['Crime', 'Drama', 'Mystery', 'Thriller', 'Film-Noir']
    elif mood == 'surprised':
        genres = ['Action', 'Adventure', 'Fantasy',
                  'Sci-Fi', 'Mystery', 'Thriller']

    return genres


def get_country(request):
    g = GeoIP2()
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1]
        country = g.country(ip)
    else:
        ip = request.META.get('REMOTE_ADDR', None)
        country = 'India'
    return country
