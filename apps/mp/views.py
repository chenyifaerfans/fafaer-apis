from django.shortcuts import render

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Banner, Profile, ProfileDetail
from .filters import ProfileDetailFilter
from .serializers import BannerSerializer, ProfileSerializer, ProfileDetailSerializer


class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        轮播图列表
    """
    queryset = Banner.objects.filter(is_del=0)
    serializer_class = BannerSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('order', )


class ProfileViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        列表
    """
    queryset = Profile.objects.filter(is_del=0)
    serializer_class = ProfileSerializer


class ProfileDetailViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        列表
    """
    queryset = ProfileDetail.objects.filter(is_del=0)
    serializer_class = ProfileDetailSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ProfileDetailFilter
    # search_fields = ('type',)
    ordering_fields = ('order',)
