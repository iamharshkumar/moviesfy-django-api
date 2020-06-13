from rest_framework import serializers
from .models import Movies, Genre, Episode


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    episode = serializers.SerializerMethodField()

    class Meta:
        model = Movies
        fields = ('id',
                  'title',
                  'story',
                  'release_date',
                  'genre',
                  'rating',
                  'image',
                  'category',
                  'create_date',
                  'trailer',
                  'type',
                  'episode'
                  )

    def get_genre(self, obj):
        q = Genre.objects.filter(movies=obj.id)
        return GenreSerializer(q, many=True).data

    def get_type(self, obj):
        return obj.get_type_display()

    def get_episode(self, obj):
        q = Episode.objects.filter(movies=obj.id)
        return EpisodeSerializer(q, many=True).data
