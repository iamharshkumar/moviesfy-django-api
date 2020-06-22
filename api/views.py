from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Movies, Genre
from .serializers import MovieSerializer, GenreSerializer

from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from django.db.models import Q
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommendedMovies(movie):
    def get_title_from_index(index):
        return df[df.index == index]["id"].values[0]

    def get_index_from_title(title):
        return (df[df.title == title]["id"].values[0]) - 1

    import pandas as pd
    qs = Movies.objects.prefetch_related('genre')

    data = [
        {'id': q.pk, 'title': q.title, 'genre': [t.genre for t in q.genre.all()], 'type': q.type,
         'category': q.category}
        for q in qs
    ]
    df = pd.DataFrame(data, columns=['id', 'title', 'genre', 'type', 'category'])

    # Step 2: Select Feature

    # Step 3: Create a column in DF which combines all selected features

    def combine_features(row):
        return row['title'] + " " + str(row['genre']) + " " + row['type'] + " " + row['category']

    df['combined_features'] = df.apply(combine_features, axis=1)

    # Step 4: Create count matrix from this new combined column
    cv = CountVectorizer()

    count_matrix = cv.fit_transform(df['combined_features'])

    # Step 5: Compute the Cosine Similarity based on the count_matrix
    cosine_sim = cosine_similarity(count_matrix)
    movie_user_likes = movie

    #  Step 6: Get index of this movie from its title
    movie_index = get_index_from_title(movie_user_likes)

    similar_movies = list(enumerate(cosine_sim[int(movie_index)]))

    # Step 7: Get a list of similar movies in descending order of similarity score
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
    new_sorted_similar_movies = sorted_similar_movies[1:]

    # Step 8: Print titles of first 50 movies
    i = 0
    movies = []
    for movie in new_sorted_similar_movies:
        # print(movie)
        movies.append(get_title_from_index(movie[0]))
        i = i + 1
        if i > 8:
            break
    return movies


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


class MovieDetail(APIView):
    serializer_class = MovieSerializer

    def get(self, request):
        q = request.GET.get('id')

        queryset = Movies.objects.all()
        queryset1 = Movies.objects.all()
        movie_list = []

        if q:
            queryset = queryset.get(id=q)
            title = queryset.title
            movies = recommendedMovies(title)
            for movie in movies:
                movie_list.append(queryset1.get(id=movie))

        serializer = self.serializer_class(queryset).data
        serializer1 = self.serializer_class(movie_list, many=True).data
        return Response({'movie_detail': serializer, 'similar_movies': serializer1}, status=HTTP_200_OK)


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
        queryset3 = []

        if movie_type:
            q = q.filter(type=movie_type)
            g = g.filter(movies__type=movie_type).order_by('id').distinct()
            queryset3 = q.filter(featured=True).order_by('-update')
            queryset1 = q.order_by('-create_date')
            queryset2 = q.order_by('-rating')

        if genre:
            q = q.filter(type=movie_type, genre=genre)
            queryset1 = q.order_by('-create_date')
            queryset2 = q.order_by('-rating')

        serializer = self.serializer_class(queryset1, many=True).data
        serializer3 = self.serializer_class(queryset3, many=True).data
        serializer1 = self.serializer_class(queryset2, many=True).data
        serializer2 = self.serializer_class1(g, many=True).data
        return Response(
            {"genres": serializer2, "featured": serializer3, "recent": serializer, "top_rated": serializer1},
            status=HTTP_200_OK)
