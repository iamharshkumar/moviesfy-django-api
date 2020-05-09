from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from api.models import Movies
from .serializers import MovieSerializer

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
