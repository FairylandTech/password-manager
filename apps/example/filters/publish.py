# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-08-04 19:39:46 UTC+08:00
"""

import django_filters

from apps.example.models.publish import PublishModel


class CharFilterInCI(django_filters.CharFilter):
    def filter(self, qs, value):
        if value in (None, ""):
            return qs
        lookup = f"{self.field_name}__icontains"
        return qs.filter(**{lookup: value})


class PublishFilter(django_filters.FilterSet):
    name = CharFilterInCI(field_name="name", lookup_expr="icontains")
    area = CharFilterInCI(field_name="area", lookup_expr="icontains")

    class Meta:
        model = PublishModel
        fields = {
            "name": ["icontains"],
            "area": ["icontains"],
            "status": ["exact"],
        }
