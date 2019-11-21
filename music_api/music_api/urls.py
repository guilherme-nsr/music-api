from django.contrib import admin
from django.urls import path
from musics.views import *

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Music API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('artists/<int:pk>/', ArtistDetail.as_view(), name=ArtistDetail.name),
    path('artists/', ArtistList.as_view(), name=ArtistList.name),
    path('albums/<int:pk>/', AlbumDetail.as_view(), name=AlbumDetail.name),
    path('albums/', AlbumList.as_view(), name=AlbumList.name),
    path('musics/<int:pk>/', MusicDetail.as_view(), name=MusicDetail.name),
    path('musics/', MusicList.as_view(), name=MusicList.name),
    path('persons/<int:pk>/', PersonDetail.as_view(), name=PersonDetail.name),
    path('persons/', PersonList.as_view(), name=PersonList.name),
    path('playlists/<int:pk>/', PlaylistDetail.as_view(), name=PlaylistDetail.name),
    path('playlists/', PlaylistList.as_view(), name=PlaylistList.name),
    path('doc/', schema_view),
    
]
