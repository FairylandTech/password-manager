# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-05 22:42:44 UTC+8
"""

import json

from rest_framework import serializers

from apps.example.models.example import Example


class TestSerializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    email = serializers.EmailField(max_length=255)
    description = serializers.CharField(required=False)
    create_time = serializers.DateTimeField(required=False)
    update_time = serializers.DateTimeField()

    def create(self, validated_data):
        return Example.objects.create(**self.validated_data)
