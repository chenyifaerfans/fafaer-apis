from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from common.permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer

User = get_user_model()


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user

        except Exception as e:
            return None


class UserViewset(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    retrieve:
    获取某一个用户信息
    """
    queryset = User.objects.filter(is_del=0)
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)


def page_forbidden(request):
    """
        全局403处理函数
        :param request:
        :return:
        """
    from django.shortcuts import render_to_response
    response = render_to_response('403.html', {})
    response.status_code = 403
    return response


def page_not_found(request):
    """
    全局404处理函数
    :param request:
    :return:
    """
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def server_error(request):
    """
        全局500处理函数
        :param request:
        :return:
        """
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response