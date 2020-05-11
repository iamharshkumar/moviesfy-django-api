from django.urls import path
from .views import MovieListView, SearchView, MovieDetail, GenreFetch

urlpatterns = [
    path('movie', MovieListView.as_view()),
    path('search', SearchView.as_view(), name='category'),
    path('movie/<pk>', MovieDetail.as_view(), name='movie-detail'),
    path('genre', GenreFetch.as_view(), name='genre-fetch'),
]
