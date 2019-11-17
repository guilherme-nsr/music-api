from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Artist, Album, Music, Person
from .serializers import ArtistSerializer, AlbumSerializer, MusicSerializer, PersonSerializer

# Create your views here.


class ArtistDetail(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    name = 'artist-detail'


class ArtistList(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    name = 'artist-list'


class AlbumDetail(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    name = 'album-detail'


class AlbumList(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    name = 'album-list'


class MusicDetail(RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    name = 'music-detail'


class MusicList(ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    name = 'music-list'


class PersonDetail(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    name = 'person-detail'


class PersonList(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    name = 'person-list'
