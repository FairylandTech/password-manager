# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-06 20:48:52 UTC+8
"""

from typing import Self, Any, Union, Dict
from datetime import datetime

import django.http.request
import rest_framework.response
from rest_framework import viewsets, mixins, status
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from apps.example.models.example import Example
from apps.example.models.generic import PublishModel, AuthorModel
from apps.example.serializers.generic import PublishSerializer, AuthorSerializer
from apps.example.serializers.test import TestSerializersV2
from utils.api import APIResults
from utils.journal import journal
from utils.pagination import StandardResultsSetPagination


class PublishViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = PublishModel.objects.all()
    serializer_class = PublishSerializer


class AuthorViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        journal.info(f"View: Author list, params: {request.query_params}")
        try:
            results = self.list(request, *args, **kwargs)
            return Response(APIResults.success(results, code=status.HTTP_200_OK), status=status.HTTP_200_OK)
        except Exception as err:
            journal.error(f"{err}")
            return Response(APIResults.error("Data does not exist."))


class PublishAPIView(GenericAPIView):

    queryset = PublishModel.objects.all()
    serializer_class = PublishSerializer

    def get(self: Self, request: Request):
        serializer: PublishSerializer = self.get_serializer(instance=self.get_queryset(), many=True)

        return Response(APIResults.success(serializer.data))

    def post(self: Self, request: Request):
        journal.info("插入一条出版社数据")
        request_data = request.data
        request_data.update(create_time=datetime.now(), update_time=datetime.now())
        journal.debug(f"校验数据: {request_data}")
        serializer: PublishSerializer = self.get_serializer(data=request_data)
        if serializer.is_valid():
            journal.info(f"校验过的数据: {serializer.validated_data}")
            serializer.save()
            return Response(APIResults.success(serializer.data))
        else:
            journal.error(serializer.errors)
            return Response(APIResults.error(serializer.errors))


class AuthorAPIView(GenericAPIView, mixins.ListModelMixin):

    queryset = AuthorModel.objects.all().order_by("-birthday", "-id")
    serializer_class = AuthorSerializer

    def get(self: Self, request: Request, *args: Any, **kwargs: Any):
        journal.info(f"View: Author list, params: {request.query_params}")
        # serializer: AuthorSerializer = self.get_serializer(instance=self.get_queryset(), many=True)
        # return Response(APIResults.success(serializer.data))
        try:
            results_mixin = self.list(request, *args, **kwargs)
            return Response(APIResults.success(results_mixin.data, code=status.HTTP_200_OK), status=status.HTTP_200_OK)
        except Exception as err:
            journal.error(f"{err}")
            return Response(APIResults.error("Data does not exist."))

    def post(self: Self, request: Request):
        journal.info(f"View: Author create: data: {request.data}")
        request_data = request.data.dict() if isinstance(request.data, django.http.request.QueryDict) else request.data
        request_data.update(create_time=datetime.now(), update_time=datetime.now())
        serializer: AuthorSerializer = self.get_serializer(data=request_data)
        if serializer.is_valid():
            journal.info(f"Validated data: {serializer.validated_data}")
            serializer.save()
            return Response(APIResults.success(serializer.data, code=status.HTTP_201_CREATED), status=status.HTTP_201_CREATED)
        else:
            journal.error(serializer.errors)
            return Response(APIResults.error(serializer.errors))


class AuthorDetailAPIView(GenericAPIView):

    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer

    def get(self: Self, request: Response, *args: Any, **kwargs: Any):
        journal.info(f"View: Author detail, pk: {repr(kwargs.get('pk'))}")
        try:
            serializer: AuthorSerializer = self.get_serializer(self.get_object(), many=False)
            return Response(APIResults.success(serializer.data))
        except Exception as err:
            journal.warning(f"{err}")
            return Response(APIResults.error("Data does not exist."))

    def _update(self: Self, request: Request, partial=False, *args: Any, **kwargs: Any):
        journal.info(f"View: Author update. Params: {args}, {kwargs}")
        try:
            instance: AuthorModel = self.get_object()
            journal.debug(f"Original Object update before: {repr(self.get_serializer(instance).data)}")
            request_data = request.data.dict() if isinstance(request.data, django.http.request.QueryDict) else request.data
            journal.debug(f"Request data: {request_data}")
            serializer: AuthorSerializer = self.get_serializer(instance, data=request_data, partial=partial)
            if serializer.is_valid():
                journal.debug(f"Validated data: {serializer.validated_data}")
                serializer.save()
                return Response(APIResults.success(serializer.data))
            else:
                journal.error(serializer.errors)
                return Response(APIResults.error(serializer.errors))
        except Exception as err:
            journal.error(f"{err}")
            return Response(APIResults.error("Data update failed."))

    def put(self: Self, request: Request, *args: Any, **kwargs: Any):
        return self._update(request, *args, **kwargs)

    def patch(self: Self, request: Request, *args: Any, **kwargs: Any):
        return self._update(request, partial=True, *args, **kwargs)

    def delete(self: Self, request: Request, *args: Any, **kwargs: Any):
        journal.info(f"View: Author delete, pk: {repr(kwargs.get('pk'))}")
        try:
            instance: AuthorModel = self.get_object()
            instance.delete()
            journal.info(f"Data deleted: {repr(instance)}")
            return Response(APIResults.success("Data deleted.", code=status.HTTP_204_NO_CONTENT), status=status.HTTP_204_NO_CONTENT)
        except Exception as err:
            journal.error(f"{err}")
            return Response(APIResults.error("Data delete failed."))


class PseudoCodeAPIViewSet(viewsets.ViewSet):

    def get_all(self: Self, request: Request):
        journal.info(f"ViewSet: AuthorAPIViewSet get all data., method: {request.method}")
        return Response(APIResults.success("Get all data."))

    def create_data(self: Self, request: Request):
        journal.info(f"ViewSet: AuthorAPIViewSet create data., method: {request.method}")
        return Response(APIResults.success("Create data."))

    def get_data(self: Self, request: Request, pk: int):
        journal.info(f"ViewSet: AuthorAPIViewSet get data by pk: {pk}, method: {request.method}")
        return Response(APIResults.success(f"Get data by pk: {pk}."))

    def update_data_all(self: Self, request: Request, pk: int):
        journal.info(f"ViewSet: AuthorAPIViewSet update data by pk: {pk}, method: {request.method}")
        return Response(APIResults.success(f"Update data all by pk: {pk}."))

    def update_data_partial(self: Self, request: Request, pk: int):
        journal.info(f"ViewSet: AuthorAPIViewSet update data partial by pk: {pk}, method: {request.method}")
        return Response(APIResults.success(f"Update data partial by pk: {pk}."))

    def delete_data(self: Self, request: Request, pk: int):
        journal.info(f"ViewSet: AuthorAPIViewSet delete data by pk: {pk}, method: {request.method}")
        return Response(APIResults.success(f"Delete data by pk: {pk}."))
