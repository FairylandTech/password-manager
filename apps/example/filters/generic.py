# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-07 01:20:59 UTC+8
"""

import django_filters

from apps.example.models.generic import PublishModel


class PublishModelFilter(django_filters.FilterSet):

    name = django_filters.CharFilter("name", lookup_expr="icontains", label="出版社名称")
    ares = django_filters.CharFilter("area", label="地区")
    # status = django_filters.BooleanFilter("expired")
    # status = django_filters.BooleanFilter("enabled")
    # status = django_filters.BooleanFilter("existence")
    status = django_filters.BooleanFilter("exist", label="数据是否存在")

    # class Meta:
    #     model = PublishModel
    #     fields = ['is_published']
