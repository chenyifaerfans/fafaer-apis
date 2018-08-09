from rest_framework import filters
from rest_framework import mixins
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Singer, Album, Audio, Song
from .serializers import SingerSerializer, AlbumSerializer, AudioSerializer, SongSerializer, AlbumListDetailSerializer, \
    AudioListDetailSerializer
from .filters import AlbumFilter, AudioFilter
from .paginations import CommonPagination


class SingerViewset(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    retrieve:
    获取歌手明细
    """
    queryset = Singer.objects.filter(is_del=0)
    serializer_class = SingerSerializer


class AlbumViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
    获取专辑列表

    retrieve:
    获取专辑明细

    """
    queryset = Album.objects.filter(is_del=0)
    pagination_class = CommonPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = AlbumFilter
    search_fields = ('name', 'desc')
    ordering_fields = ('add_time',)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AlbumListDetailSerializer
        return AlbumSerializer


class AudioViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
    获取电台列表

    retrieve:
    获取电台明细

    """
    queryset = Audio.objects.filter(is_del=0)
    pagination_class = CommonPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = AudioFilter
    search_fields = ('name', 'desc')
    ordering_fields = ('add_time',)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AudioListDetailSerializer
        return AudioSerializer


class SongViewset(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    retrieve:
    获取歌曲明细

    """
    queryset = Song.objects.filter(is_del=0)
    serializer_class = SongSerializer
