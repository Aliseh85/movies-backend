from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    vote_average = models.FloatField()
    poster_path = models.ImageField(upload_to='posters/')  # For poster images

    def __str__(self):
        return self.title
