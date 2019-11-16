from rest_framework.serializers import HyperlinkedModelSerializer, SlugRelatedField
from .models import Artist, Album, Music


class ArtistSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('url', 'pk', 'name', 'debut_year')


class AlbumSerializer(HyperlinkedModelSerializer):
    artist = SlugRelatedField(queryset=Artist.objects.all(), slug_field='name')

    class Meta:
        model = Album
        fields = ('url', 'pk', 'title', 'genre', 'year', 'artist')


class MusicSerializer(HyperlinkedModelSerializer):
    album = SlugRelatedField(queryset=Album.objects.all(), slug_field='title')

    class Meta:
        model = Music
        fields = ('url', 'pk', 'title', 'length', 'album')
