from django.db import models
from django.utils.html import format_html
from django.urls import reverse



class Artist(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    cover = models.ImageField(upload_to="covers/", blank=True, null=True)
    image = models.ImageField(upload_to='album_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=10, blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def admin_link(self):
        url = reverse("admin:albums_song_change", args=[self.id])
        return format_html('<a href="{}">{}</a>', url, self.title)


# Create your models here.
