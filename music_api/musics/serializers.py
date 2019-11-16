from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Artist, Album


class ArtistSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('url', 'pk', 'name', 'debut_year')
