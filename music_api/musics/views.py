from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import *
from .serializers import *
from .permissions import *
from rest_framework.throttling import ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import rest_framework.permissions



class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
                'artists' : reverse(ArtistList.name, request=request),
                'albums' : reverse(AlbumList.name, request=request),
                'musics' : reverse(MusicList.name, request=request),
                'persons' : reverse(PersonList.name, request=request),
                'playlists' : reverse(PlaylistList.name, request=request),
        })


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    name = 'artist-detail'
    permission_classes = [IsAdminOrReadOnly]

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    name = 'artist-list'
    permission_classes = [IsAdminOrReadOnly]

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    name = 'album-detail'
    permission_classes = [IsAdminOrReadOnly]

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    name = 'album-list'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['artist']
    search_fields = ['title']
    ordering_fields = ['title']
    permission_classes = [IsAdminOrReadOnly]

class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    name = 'music-detail'
    permission_classes = [IsAdminOrReadOnly]


class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    name = 'music-list'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['album']
    search_fields = ['title']
    ordering_fields = ['title']
    permission_classes = [IsAdminOrReadOnly]


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    name = 'person-detail'
    throttle_scope = 'users'
    throttle_classes = (ScopedRateThrottle,)
    permission_classes = [IsOwnerOrReadOnly]

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    name = 'person-list'
    throttle_scope = 'users'
    throttle_classes = (ScopedRateThrottle,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    name = 'playlist-detail'
    throttle_scope = 'playlists'
    throttle_classes = (ScopedRateThrottle,)
    permission_classes = [IsOwnerOrReadOnly]
    


class PlaylistList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    name = 'playlist-list'
    throttle_scope = 'playlists'
    throttle_classes = (ScopedRateThrottle,)
    permission_classes = [permissions.IsAuthenticated]
