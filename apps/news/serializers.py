# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/9/8 16:44'
from users.serializers import UserSerializer2
from common.base import CommonSerializer
from .models import Banner, Article, Topic, Recommend, TopicDetail, RecommendDetail


class BannerSerializer(CommonSerializer):
    user = UserSerializer2()

    class Meta:
        model = Banner
        exclude = ('is_del', 'add_time', 'update_time')


class ArticleSerializer(CommonSerializer):
    user = UserSerializer2()

    class Meta:
        model = Article
        exclude = ('is_del', 'add_time', 'update_time')


class TopicSerializer(CommonSerializer):
    user = UserSerializer2()

    class Meta:
        model = Topic
        exclude = ('is_recommend', 'is_del', 'add_time', 'update_time')


class TopicDetailSerializer(CommonSerializer):
    user = UserSerializer2()
    article = ArticleSerializer(many=False)

    class Meta:
        model = TopicDetail
        exclude = ('topic', 'is_del', 'add_time', 'update_time')


class TopicSerializer2(CommonSerializer):
    user = UserSerializer2()
    topics = TopicDetailSerializer(many=True)

    class Meta:
        model = Topic
        exclude = ('is_recommend', 'is_del', 'add_time', 'update_time')


class RecommendSerializer(CommonSerializer):
    user = UserSerializer2()

    class Meta:
        model = Recommend
        exclude = ('is_recommend', 'is_del', 'add_time', 'update_time')


class RecommendDetailSerializer(CommonSerializer):
    user = UserSerializer2()
    article = ArticleSerializer(many=False)

    class Meta:
        model = RecommendDetail
        exclude = ('recommend', 'is_del', 'add_time', 'update_time')


class RecommendSerializer2(CommonSerializer):
    user = UserSerializer2()
    recommends = RecommendDetailSerializer(many=True)

    class Meta:
        model = Recommend
        exclude = ('is_recommend', 'is_del', 'add_time', 'update_time')
