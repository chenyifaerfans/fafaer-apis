"""fafaerapis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from mp.views import BannerViewset, ProfileViewset, ProfileDetailViewset
from music.views import SingerViewset, AlbumViewset, AudioViewset, SongViewset

import xadmin

router = DefaultRouter()
router.register(r'mp/banner', BannerViewset, base_name='banner')
router.register(r'mp/profile', ProfileViewset, base_name='profile')
router.register(r'mp/detail', ProfileDetailViewset, base_name='detail')
router.register(r'music/singer', SingerViewset, base_name='singer')
router.register(r'music/album', AlbumViewset, base_name='album')
router.register(r'music/audio', AudioViewset, base_name='audio')
router.register(r'music/song', SongViewset, base_name='song')

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^docs/', include_docs_urls(title='文档')),

    url(r'^api-auth/', include('rest_framework.urls')),

    url(r'^', include(router.urls))
]
