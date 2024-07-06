# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-15 15:11:56 UTC+8
"""

from rest_framework import viewsets, mixins

from apps.example.models.example import Example
from apps.example.serializers.example import ExampleSerializer


class ExampleViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
