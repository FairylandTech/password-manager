# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-05 20:19:31 UTC+8
"""

from typing import Self

from django.views.generic.base import View
from django.http.response import HttpResponse

from rest_framework.views import APIView
from rest_framework.request import Request

from apps.example.models.example import Example
from apps.example.serializers.test import TestSerializers, TestSerializersV2
from utils.journal import journal
from rest_framework.response import Response

from utils.api import APIResults


class Test(APIView):

    def get(self: Self, request: Request):
        data_id = request.query_params.get("id")
        if data_id:
            journal.info("获取一条数据")
            example = Example.objects.filter(status=True).get(pk=data_id)
            _many = False
        else:
            journal.info("获取全部数据")
            example = Example.objects.filter(status=True).all().order_by("id")
            _many = True
        # serializer = TestSerializers(example, many=_many)
        serializer = TestSerializersV2(example, many=_many)

        return Response(APIResults.success(serializer.data))

    def post(self: Self, request: Request):
        journal.info("提交一个数据")
        data = request.data
        from datetime import datetime

        data.update(create_time=datetime.now(), update_time=datetime.now())
        journal.debug(f"拿到的数据: {data}")
        # serializer = TestSerializers(data=data)
        serializer = TestSerializersV2(data=data)
        if serializer.is_valid():
            journal.info(f"校验过的数据: {serializer.validated_data}")
            serializer.save()
            return Response(APIResults.success(serializer.data))
        else:
            journal.error(serializer.errors)
            return Response(APIResults.error(serializer.errors))

    def put(self: Self, request: Request):
        journal.info("修改一条数据")
        request_data = request.data
        pk_id = request_data.get("id")
        if pk_id:
            from datetime import datetime

            request_data.update(update_time=datetime.now())
            example = Example.objects.get(pk=pk_id)
            # serializer = TestSerializers(example, data=request_data)
            serializer = TestSerializersV2(example, data=request_data)
            if serializer.is_valid():
                serializer.save()
                return Response(APIResults.success(serializer.data))
            else:
                return Response(APIResults.error(serializer.errors))
        else:
            return Response(APIResults.error("Request data need id."))

    def delete(self: Self, request: Request):
        journal.info("删除一条数据")
        request_data = request.query_params
        journal.debug(f"拿到的数据: {request_data}")
        pk_id = request_data.get("id")
        if pk_id:
            if Example.objects.filter(pk=pk_id).update(status=False):
                return Response(APIResults.success())
            else:
                return Response(APIResults.error("Delete failed."))
        else:
            return Response(APIResults.error("Request data need id."))
