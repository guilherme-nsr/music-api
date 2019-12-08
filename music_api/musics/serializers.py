from rest_framework.serializers import HyperlinkedModelSerializer, SlugRelatedField, ModelSerializer
from .models import Artist, Album, Music, Person, Playlist

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)


class MusicSerializer(HyperlinkedModelSerializer):
    album = SlugRelatedField(queryset=Album.objects.all(), slug_field='title')
    artist = SlugRelatedField(queryset=Artist.objects.all(), slug_field='name')

    class Meta:
        model = Music
        fields = ('url', 'pk', 'title', 'length', 'album', 'artist')


class AlbumSerializer(HyperlinkedModelSerializer):
    artist = SlugRelatedField(queryset=Artist.objects.all(), slug_field='name')
    musics = MusicSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('url', 'pk', 'title', 'genre', 'year', 'artist', 'musics')


class ArtistSerializer(HyperlinkedModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('url', 'pk', 'name', 'debut_year', 'albums')


class PersonSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('url', 'pk', 'username', 'full_name')


class PlaylistSerializer(HyperlinkedModelSerializer):
    author = PersonSerializer()
    musics = MusicSerializer(many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = ('url', 'pk', 'title', 'author', 'musics')
