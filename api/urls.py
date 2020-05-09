from django.urls import path
from .views import MovieListView, SearchView, MovieDetail

urlpatterns = [
    path('movie', MovieListView.as_view()),
    path('search', SearchView.as_view(), name='category'),
    path('movie/<pk>', MovieDetail.as_view(), name='movie-detail'),
]
