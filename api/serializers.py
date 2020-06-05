from rest_framework import serializers
from api.models import Movies, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    class Meta:
        model = Movies
        fields = ('id',
                  'title',
                  'story',
                  'release_date',
                  'genre',
                  'rating',
                  'image',
                  'download',
                  'category',
                  'create_date',
                  'trailer',
                  'download_size',
                  'type')

    def get_genre(self, obj):
        q = Genre.objects.filter(movies=obj.id)
        return GenreSerializer(q, many=True).data

    def get_type(self, obj):
        return obj.get_type_display()
