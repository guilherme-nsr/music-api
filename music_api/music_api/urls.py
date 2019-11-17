"""music_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from musics.views import ArtistDetail, ArtistList, AlbumDetail, AlbumList, MusicDetail, MusicList, PersonDetail, PersonList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artists/<int:pk>/', ArtistDetail.as_view(), name=ArtistDetail.name),
    path('artists/', ArtistList.as_view(), name=ArtistList.name),
    path('albums/<int:pk>/', AlbumDetail.as_view(), name=AlbumDetail.name),
    path('albums/', AlbumList.as_view(), name=AlbumList.name),
    path('musics/<int:pk>/', MusicDetail.as_view(), name=MusicDetail.name),
    path('musics/', MusicList.as_view(), name=MusicList.name),
    path('persons/<int:pk>/', PersonDetail.as_view(), name=PersonDetail.name),
    path('persons/', PersonList.as_view(), name=PersonList.name)
]
