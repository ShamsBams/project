from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Music(models.Model):
    rate_choice = {
        (1, 'one'),
        (2, 'two'),
        (3, 'three'),
        (4, 'four'),
        (5, 'five'),
    }
    title = models.CharField(max_length=40)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    urls = models.URLField()
    musician = models.ForeignKey('Musician', on_delete=models.CASCADE)
    rate = models.CharField(max_length=1, choices=rate_choice)

    def __str__(self):
        return "{}, {} ".format(self.title, self.musician)


class Musician(models.Model):
    country = models.CharField(max_length=38, blank=True, null=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthday = models.DateField(blank=True, null=True)
    alive = models.BooleanField()

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)