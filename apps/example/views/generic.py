# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-06 20:48:52 UTC+8
"""

from typing import Self
from datetime import datetime

from rest_framework import viewsets, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from apps.example.models.example import Example
from apps.example.models.generic import PublishModel, AuthorModel
from apps.example.serializers.generic import PublishSerializers, AuthorSerializers
from apps.example.serializers.test import TestSerializersV2
from utils.api import ApiResponse
from utils.journal import journal


class PublishViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = PublishModel.objects.all()
    serializer_class = PublishSerializers


class AuthorViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializers


class PublishAPIView(GenericAPIView):

    queryset = PublishModel.objects.all()
    serializer_class = PublishSerializers

    def get(self: Self, request: Request):
        serializer: PublishSerializers = self.get_serializer(instance=self.get_queryset(), many=True)

        return Response(ApiResponse(serializer.data).results)

    def post(self: Self, request: Request):
        journal.info("插入一条出版社数据")
        request_data = request.data.dict()
        request_data.update(create_time=datetime.now(), update_time=datetime.now())
        journal.debug(f"校验数据: {request_data}")
        serializer: PublishSerializers = self.get_serializer(data=request_data)
        if serializer.is_valid():
            journal.info(f"校验过的数据: {serializer.validated_data}")
            serializer.save()
            return Response(ApiResponse(serializer.data).results)
        else:
            journal.error(serializer.error_messages)
            return Response(ApiResponse(serializer.errors).results)


class AuthorAPIView(GenericAPIView):

    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializers

    def get(self: Self, request: Request):
        serializer: PublishSerializers = self.get_serializer(instance=self.get_queryset(), many=True)

        return Response(ApiResponse(serializer.data).results)

    def post(self: Self, request: Request):
        journal.info("插入一条作者数据")
        request_data = request.data.dict()
        request_data.update(create_time=datetime.now(), update_time=datetime.now())
        journal.debug(f"校验数据: {request_data}")
        serializer: PublishSerializers = self.get_serializer(data=request_data)
        if serializer.is_valid():
            journal.info(f"校验过的数据: {serializer.validated_data}")
            serializer.save()
            return Response(ApiResponse(serializer.data).results)
        else:
            journal.error(serializer.error_messages)
            return Response(ApiResponse(serializer.errors).results)
