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
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from django.views.static import serve

from fafaerapis.settings import MEDIA_ROOT
from fafaerapis.settings import DEBUG

from users.views import UserViewset
from mp.views import BannerViewset, ProfileViewset, ProfileDetailViewset
from appintro.views import AppIntroViewset
from news.views import BannerViewset as ArticleBannerViewset, ArticleViewset, TopicViewset, RecommendViewset
from music.views import SingerViewset, AlbumViewset, AudioViewset, SongViewset, AlbumDetailViewset, AudioDetailViewset
from photos.views import GalleryViewset, PhotoViewset, GalleryDetailViewset
from videos.views import VideoCollectionViewset, VideoViewset, VideoCollectionDetailViewset

import xadmin

router = DefaultRouter()
router.register(r'users/user', UserViewset, base_name='user')

router.register(r'mp/banner', BannerViewset, base_name='banner')
router.register(r'mp/profile', ProfileViewset, base_name='profile')
router.register(r'mp/detail', ProfileDetailViewset, base_name='mp_detail')

router.register(r'app/intro', AppIntroViewset, base_name='app_intro')

router.register(r'news/articles', ArticleViewset, base_name='news_articles')
router.register(r'news/banners', ArticleBannerViewset, base_name='news_banners')
router.register(r'news/topics', TopicViewset, base_name='news_topics')
router.register(r'news/recommends', RecommendViewset, base_name='news_recommends')

router.register(r'music/singer', SingerViewset, base_name='singer')
router.register(r'music/album', AlbumViewset, base_name='album')
router.register(r'music/album_detail', AlbumDetailViewset, base_name='album_detail')
router.register(r'music/audio', AudioViewset, base_name='audio')
router.register(r'music/audio_detail', AudioDetailViewset, base_name='audio_detail')
router.register(r'music/song', SongViewset, base_name='song')

router.register(r'photos/gallery', GalleryViewset, base_name='gallery')
router.register(r'photos/photo', PhotoViewset, base_name='photo')
router.register(r'photos/detail', GalleryDetailViewset, base_name='detail')

router.register(r'videos/collection', VideoCollectionViewset, base_name='collection')
router.register(r'videos/video', VideoViewset, base_name='video')
router.register(r'videos/detail', VideoCollectionDetailViewset, base_name='collection_detail')

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),

    #
    url(r'^ueditor/', include('DjangoUeditor.urls')),

    #
    url(r'^', include_docs_urls(title='文档', public=False)),
    url(r'^api-auth/', include('rest_framework.urls')),

    # drf自带的token认证模式
    url(r'^drf-auth/', obtain_auth_token),

    # JWT token认证模式
    url(r'^login/auth/', obtain_jwt_token),
    url(r'^jwt/refresh/', refresh_jwt_token),
    url(r'^jwt/verify/', verify_jwt_token),

    url(r'^v1/', include(router.urls, namespace='v1')),

    # 配置上传文件的处理
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

]

if not DEBUG:
    from fafaerapis.settings import STATIC_ROOT
    urlpatterns += [
        # settings中DEBUG为False时，必须设置
        url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
    ]


# 全局403页面配置
handler403 = 'users.views.page_forbidden'

# 全局404页面配置
handler404 = 'users.views.page_not_found'

# 全局500页面配置
handler500 = 'users.views.server_error'
