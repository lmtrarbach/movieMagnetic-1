from __future__ import unicode_literals

from django.db import models

# Campos da pagina inicial

class genreGames(models.Model):
	genre = models.CharField(max_length=64)
class plataformGames(models.Model):
	plataform = models.CharField(max_length=64)

class genreSeries(models.Model):
	genre = models.CharField(max_length=64)

class genreMovies(models.Model):
        genre = models.CharField(max_length=64)

