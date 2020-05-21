from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from api.models import Movies, Genre
from .serializers import MovieSerializer, GenreSerializer

from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from django.db.models import Q


# Create your views here.
class SearchView(APIView):
    serializer_class = MovieSerializer

    def get(self, request):
        queryset = Movies.objects.all()
        query = request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
            )
        serializer = self.serializer_class(queryset, many=True).data
        return Response(serializer, status=HTTP_200_OK)


class MovieListView(ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class GenreList(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreFetch(APIView):
    serializer_class = MovieSerializer

    def get(self, request):
        queryset = Movies.objects.all()
        q = request.GET.get('q')

        if q:
            queryset = queryset.filter(genre=q)
        serializer = self.serializer_class(queryset, many=True).data
        return Response(serializer, status=HTTP_200_OK)


class FetchCategoryType(APIView):
    serializer_class = MovieSerializer

    def get(self, request):
        queryset = Movies.objects.all()
        genre = request.GET.get('genre')
        movie_type = request.GET.get('type')
        queryset1 = []
        queryset2 = []

        if movie_type:
            queryset = queryset.filter(type=movie_type)
            queryset1 = queryset.order_by('-create_date')
            queryset2 = queryset.order_by('-rating')

        if genre:
            queryset = queryset.filter(type=movie_type, genre=genre)
            queryset1 = queryset.order_by('-create_date')
            queryset2 = queryset.order_by('-rating')

        serializer = self.serializer_class(queryset1, many=True).data
        serializer1 = self.serializer_class(queryset2, many=True).data
        return Response({"recent": serializer, "top_rated": serializer1}, status=HTTP_200_OK)
