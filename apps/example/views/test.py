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
from apps.example.serializers.test import TestSerializers
from utils.journal import journal
from rest_framework.response import Response

from utils.api import ApiResponse


class Test(APIView):

    def get(self: Self, request: Request):
        data_id = request.query_params.get("id")
        if data_id:
            journal.info("获取一条数据")
            example = Example.objects.get(pk=data_id)
            _many = False
        else:
            journal.info("获取全部数据")
            example = Example.objects.all()
            _many = True
            journal.info(f"{example}, 类型: {type(example)}")
        serializer = TestSerializers(example, many=_many)
        return Response(ApiResponse(serializer.data).results)

    def post(self: Self, request: Request):
        journal.info("提交一个数据")
        data = request.data
        from datetime import datetime
        data.update(
            create_time=datetime.now().strftime("%Y-%d-%m %H:%M:%S"),
            update_time=datetime.now().strftime("%Y-%d-%m %H:%M:%S")
        )
        journal.debug(f"拿到的数据: {data}")
        serializer = TestSerializers(data=data)
        if serializer.is_valid():
            journal.info(f"校验过的数据: {serializer.validated_data}")
            serializer.save()
            return Response(ApiResponse(serializer.data).results)
        else:
            return Response(ApiResponse(serializer.error_messages).results)

    def put(self: Self, request: Request):
        journal.info("修改一条数据")
        request_data = request.data
        if request_data:
            pk_id = request_data.pop("id")
            from datetime import datetime
            request_data.update(update_time=datetime.now().strftime("%Y-%d-%m %H:%M:%S"))
            example = Example.objects.get(pk=pk_id)
            serializer = TestSerializers(example, data=request_data)
            if serializer.is_valid():
                Example.objects.filter(pk=pk_id).update(**serializer.validated_data)
                rdata = Example.objects.get(pk=pk_id)
                return Response(ApiResponse(TestSerializers(rdata, many=False).data).results)
            else:
                return Response(ApiResponse(serializer.error_messages).results)
        else:
            return Response(ApiResponse("需要一个ID参数").results)
"""
{
    "id": 2,
    "age": 21,
    "description": "我是Alice--修改之后的"
}
"""
