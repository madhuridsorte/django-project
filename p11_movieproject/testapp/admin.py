from django.contrib import admin
from testapp.models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ['rdate', 'movie_name', 'actor', 'actress', 'rating']
    
admin.site.register(Movie, MovieAdmin)