# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-08-04 18:41:07 UTC+08:00
"""

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend

from apps.example.models.publish import PublishModel
from apps.example.serializers.publish import PublishSerializer
from apps.example.filters.publish import PublishFilter

from utils.journal import journal


class PublishAPIView(GenericAPIView):
    queryset = PublishModel.objects.all()
    serializer_class = PublishSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PublishFilter

    def get(self, request: Request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer: PublishSerializer = self.get_serializer(instance=queryset, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        payload = request.data
        serializer: PublishSerializer = self.get_serializer(data=payload)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
