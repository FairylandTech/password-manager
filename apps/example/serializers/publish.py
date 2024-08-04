# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-08-04 18:25:53 UTC+08:00
"""

from rest_framework import serializers
from apps.example.models.publish import AuthorModel
from apps.example.models.publish import PublishModel

from fairylandfuture.constants.enums import DateTimeEnum


class PublishSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, label="出版社名字")
    area = serializers.CharField(max_length=255, label="出版社地区", required=False, allow_blank=True, allow_null=True)
    status = serializers.BooleanField(read_only=True, label="数据状态", required=False)
    create_time = serializers.DateTimeField(read_only=True, label="创建时间", format=DateTimeEnum.default(), required=False)
    update_time = serializers.DateTimeField(read_only=True, label="修改事件", format=DateTimeEnum.default())

    class Meta:
        model = PublishModel
        fields = ("id", "name", "area", "status", "create_time", "update_time")
