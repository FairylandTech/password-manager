# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-05 22:42:44 UTC+8
"""

import json

from typing import Dict, Any

from rest_framework import serializers

from apps.example.models.example import Example


class TestSerializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    email = serializers.EmailField(max_length=255)
    status = serializers.BooleanField(required=False, default=True)
    description = serializers.CharField(required=False, default=None)
    create_time = serializers.DateTimeField(required=False, format="%Y-%m-%d %H:%M:%S")
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    def create(self, validated_data: Dict[str, Any]):
        return Example.objects.create(**validated_data)

    def update(self, instance: Example, validated_data: Dict[str, Any]):
        Example.objects.filter(pk=instance.pk).update(**validated_data)
        return Example.objects.get(pk=instance.pk)


class TestSerializersV2(serializers.ModelSerializer):
    is_status = serializers.BooleanField(source="status", required=False)
    create_time = serializers.DateTimeField(required=False, format="%Y-%m-%d %H:%M:%S")
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Example
        # fields = "__all__"
        exclude = ["status"]
