from django.contrib import admin

from .models import Movie,Kind,Editor,Director,Actor,Language,Country

class movieadmin(admin.ModelAdmin):
    list_display = ('movie_name', 'directors','editors','actors','kinds','countrys','languages', 'release_date','runtime',
                    'nickname','imdb','rating_num','votes',)
    search_fields = ('movie_name', 'director','editor','actor','kind','country','language',
                    'nickname','imdb','rating_num',)

class kindadmin(admin.ModelAdmin):
    list_display = ('kind','movie_name', )
    search_fields = ('movie_name__movie_name', 'kind',)

class editoradmin(admin.ModelAdmin):
    list_display = ('editor','movie_name', )
    search_fields = ('movie_name__movie_name', 'editor',)

class directoradmin(admin.ModelAdmin):
    list_display = ('director','movie_name', )
    search_fields = ('movie_name__movie_name', 'director',)

class countryadmin(admin.ModelAdmin):
    list_display = ('country','movie_name', )
    search_fields = ('movie_name__movie_name', 'director',)

class actoradmin(admin.ModelAdmin):
    list_display = ('actor','movie_name', )
    search_fields = ('movie_name__movie_name', 'actor',)

class languageadmin(admin.ModelAdmin):
    list_display = ('language','movie_name', )
    search_fields = ('movie_name__movie_name', 'language',)

# Register your models here.
admin.site.register(Movie,movieadmin)
admin.site.register(Kind,kindadmin)
admin.site.register(Director,directoradmin)
admin.site.register(Editor,editoradmin)
admin.site.register(Actor,actoradmin)
admin.site.register(Country,countryadmin)
admin.site.register(Language,languageadmin)





