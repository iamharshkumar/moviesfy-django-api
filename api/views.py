from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .models import Movies, Genre
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
    serializer_class1 = GenreSerializer

    def get(self, request):
        q = Movies.objects.all()
        g = Genre.objects.all()
        genre = request.GET.get('genre')
        movie_type = request.GET.get('type')
        queryset1 = []
        queryset2 = []

        if movie_type:
            q = q.filter(type=movie_type)
            g = g.filter(movies__type=movie_type).order_by('id').distinct()
            queryset1 = q.order_by('-create_date')
            queryset2 = q.order_by('-rating')

        if genre:
            q = q.filter(type=movie_type, genre=genre)
            queryset1 = q.order_by('-create_date')
            queryset2 = q.order_by('-rating')

        serializer = self.serializer_class(queryset1, many=True).data
        serializer1 = self.serializer_class(queryset2, many=True).data
        serializer2 = self.serializer_class1(g, many=True).data
        return Response({"genres":serializer2,"recent": serializer, "top_rated": serializer1}, status=HTTP_200_OK)
