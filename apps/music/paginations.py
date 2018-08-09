# _*_ coding:utf-8 _*_
__author__ = 'WANGY'
__date__ = '2018/8/9 12:43'

from rest_framework import pagination


class CommonPagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = 100
