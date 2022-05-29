from django.contrib import admin

# Register your models here.
from .models import Movie, Genre, Keyword, Users, Rating

admin.site.site_header = 'Movie Database Administration'
admin.site.site_title = 'Movie Database Admin'
admin.site.index_title = 'Manage your Movies'

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Keyword)
admin.site.register(Users)
admin.site.register(Rating)
