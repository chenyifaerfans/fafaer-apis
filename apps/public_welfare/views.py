from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from common.permissions import IsOwnerOrReadOnly
from .models import Lost
from .paginations import CommonPagination
from .serializers import LostSerializer


class LostViewset(viewsets.ModelViewSet):
    """
    视频合集

    list:
    获取视频合集列表

    retrieve:
    获取视频合集明细

    create:
    创建视频合集

    update:
    更新视频合集

    destroy：
    删除视频合集

    """
    queryset = Lost.objects.filter(is_del=0)
    pagination_class = CommonPagination
    serializer_class = LostSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'desc', 'lost_location')
    ordering_fields = ('add_time',)

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action == "update" or self.action == "partial_update" or self.action == "destroy":
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return super(LostViewset, self).get_permissions()
