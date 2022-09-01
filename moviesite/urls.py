
from django.urls import path, re_path
from moviesite.views import *

urlpatterns = [
    path('', MainViewHome.as_view(), name='main_page'),
    path('Movie/<slug:slug_movie>/', MovieView.as_view(), name='movie'),
    path('Genre/<slug:slug_cat>/', CategoriesView.as_view(), name='categories')
]