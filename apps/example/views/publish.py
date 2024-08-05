# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-08-04 18:41:07 UTC+08:00
"""

from typing import Dict

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend

from apps.example.models.publish import PublishModel
from apps.example.serializers.publish import PublishSerializer
from apps.example.filters.publish import PublishFilter

from utils.journal import journal
from utils.exceptions import RequestParametersMissing


class PublishAPIView(GenericAPIView):
    queryset = PublishModel.objects.all().filter(status=True)
    serializer_class = PublishSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PublishFilter

    def validate_id(self, payload: Dict):
        if "id" not in payload.keys():
            raise RequestParametersMissing("Request parameter 'id' missing.")

        return payload

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

    def put(self, request: Request):
        try:
            payload: Dict = self.validate_id(request.data)

            publish = PublishModel.objects.get(id=payload.pop("id"))
            serializer: PublishSerializer = self.get_serializer(instance=publish, data=payload)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except RequestParametersMissing as err:
            journal.error(f"err: {err}, type: {type(err)}")
            return Response({"message": err.message, "code": 400})

    def delete(self, request: Request):
        try:
            payload: Dict = self.validate_id(request.data)

            publish = PublishModel.objects.get(id=payload.pop("id"))
            publish.status = False
            publish.save()
            return Response({"message": "Delete success.", "code": 200})
        except Exception as err:
            journal.error(f"err: {err}, type: {type(err)}")
            return Response({"message": "", "code": 400})
