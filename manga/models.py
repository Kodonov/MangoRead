from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name

class Manga(models.Model):
    eng_name = models.CharField(max_length=100, default='')
    rus_name = models.CharField(max_length=100,default='')
    dir = models.CharField(max_length=250, null=True, blank=True)
    issue_year = models.PositiveSmallIntegerField(null=True)
    avg_rating = models.FloatField(default=0.0, blank=True)
    admin_rating = models.FloatField(default=0.0, blank=True)
    type = models.CharField(max_length=100)
    poster = models.TextField(default='', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    chapters_quantity = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Манга"
        verbose_name_plural = "Манги"

    def __str__(self):
        return self.rus_name



