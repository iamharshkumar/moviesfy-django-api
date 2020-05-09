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
    genre = models.ManyToManyField(to=Genre, null=True)
    rating = models.DecimalField(decimal_places=1, max_digits=5)
    image = models.CharField(max_length=2000, null=False)
    download = models.FileField()
    category = models.CharField(max_length=100, choices=(("B", "Bollywood"), ('H', "Hollywood")))
    create_date = models.DateTimeField(auto_now_add=True)
    trailer = models.CharField(max_length=500, null=True, blank=True)
    download_size = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
