from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=200)
    debut_year = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Album(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    year = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums', default=None)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Music(models.Model):
    title = models.CharField(max_length=200)
    length = models.PositiveIntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musics', default=None)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Person(models.Model):
    full_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('username',)


class Playlist(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='playlists', default=None)
    musics = models.ManyToManyField(Music, related_name='playlists')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
