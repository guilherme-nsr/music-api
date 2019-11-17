from rest_framework.serializers import HyperlinkedModelSerializer, SlugRelatedField
from .models import Artist, Album, Music, Person, Playlist


class AlbumSerializer(HyperlinkedModelSerializer):
    artist = SlugRelatedField(queryset=Artist.objects.all(), slug_field='name')

    class Meta:
        model = Album
        fields = ('url', 'pk', 'title', 'genre', 'year', 'artist')


class ArtistSerializer(HyperlinkedModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('url', 'pk', 'name', 'debut_year', 'albums')


class MusicSerializer(HyperlinkedModelSerializer):
    album = SlugRelatedField(queryset=Album.objects.all(), slug_field='title')

    class Meta:
        model = Music
        fields = ('url', 'pk', 'title', 'length', 'album')


class PersonSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('url', 'pk', 'username', 'full_name')


class PlaylistSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
        fields = ('url', 'pk', 'title', 'author', 'musics')
