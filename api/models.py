from django.db import models


# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre


class Movies(models.Model):
    title = models.CharField(max_length=250, null=False)
    story = models.CharField(max_length=2000, null=False)
    release_date = models.CharField(max_length=100, null=False)
    genre = models.ManyToManyField(to=Genre, blank=True)
    rating = models.DecimalField(decimal_places=1, max_digits=5, default=0)
    image = models.CharField(max_length=2000, null=False)
    category = models.CharField(max_length=100, choices=(("Bollywood", "Bollywood"), ('Hollywood', "Hollywood")))
    create_date = models.DateTimeField(auto_now_add=True)
    trailer = models.CharField(max_length=500, null=True, blank=True)
    type = models.CharField(max_length=100, choices=(("Movie", "Movie"), ("Season", "Season")), null=True, blank=True)
    featured = models.BooleanField(default=False, null=True, blank=True)
    update = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title


class Episode(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    download = models.CharField(max_length=2000)
    download_size = models.CharField(max_length=100, null=True, blank=True)
    quality = models.CharField(max_length=50,
                               choices=(("360p", "360p"), ("480p", "480p"), ("720p", "720p"), ("1080p", "1080p")),
                               null=True, blank=True)
    length = models.CharField(max_length=100, null=True, blank=True)
    movies = models.ForeignKey(Movies, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
