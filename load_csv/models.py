from platform import release
from django.db import models
from django.forms import CharField

# Create your models here.
class Movies(models.Model):
    show_id = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=200, null=True, default=None)
    cast = models.TextField()
    release_year = models.IntegerField()

