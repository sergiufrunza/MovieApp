from django.contrib import admin
from .models import *


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(UserProfile)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Countries)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Years)
admin.site.register(FilmDirectors)
admin.site.register(MovieData)
admin.site.register(Actors)


