from django.urls import path
from .views import MovieListView, SearchView, MovieDetail, GenreFetch, GenreList, FetchCategoryType

urlpatterns = [
    # path('movie', MovieListView.as_view()),
    path('search', SearchView.as_view(), name='search-title'),
    path('movie', MovieDetail.as_view(), name='movie-detail'),
    path('genre/search', GenreFetch.as_view(), name='genre-fetch'),
    path('genre/list', GenreList.as_view(), name='genre-list'),
    path('fetch/', FetchCategoryType.as_view(), name='fetch-movie'),
]
