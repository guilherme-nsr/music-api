from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *
from .permissions import *
from rest_framework.throttling import ScopedRateThrottle


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
    permission_classes = (IsAdminOrReadOnly,)

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    name = 'artist-list'
    permission_classes = (IsAdminOrReadOnly,)

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    name = 'album-detail'
    permission_classes = (IsAdminOrReadOnly,)

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    name = 'album-list'
    permission_classes = (IsAdminOrReadOnly,)

class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    name = 'music-detail'
    permission_classes = (IsAdminOrReadOnly,)


class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    name = 'music-list'
    permission_classes = (IsAdminOrReadOnly,)


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    name = 'person-detail'
    permission_classes = (IsOwnerOrReadOnly,)
    throttle_scope = 'users'
    throttle_classes = (ScopedRateThrottle,)

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    name = 'person-list'
    throttle_scope = 'users'
    throttle_classes = (ScopedRateThrottle,)


class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    name = 'playlist-detail'
    permission_classes = (IsOwnerOrReadOnly,)
    throttle_scope = 'playlists'
    throttle_classes = (ScopedRateThrottle,)


class PlaylistList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    name = 'playlist-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_scope = 'playlists'
    throttle_classes = (ScopedRateThrottle,)
