# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-06 23:45:52 UTC+8
"""

from datetime import datetime

from rest_framework import serializers

from apps.example.models.generic import PublishModel, AuthorModel


class AuthorModelGenderField(serializers.Field):

    def to_representation(self, value):
        return "男" if value else "女"

    def to_internal_value(self, data):
        if data in ("男", 0, True):
            return True
        elif data in ("女", 1, False):
            return False
        else:
            raise serializers.ValidationError("性别必须是 '男' 或 '女'")


class PublishSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(required=False, read_only=True, format="%Y-%d-%m %H:%M:%S")
    update_time = serializers.DateTimeField(read_only=True, format="%Y-%d-%m %H:%M:%S")

    class Meta:
        model = PublishModel
        # fields = "__all__"
        exclude = ("status",)
        read_only_fields = ("create_time", "update_time")

    def create(self, validated_data):
        return PublishModel.objects.create(**validated_data)


class AuthorSerializer(serializers.ModelSerializer):
    gender = AuthorModelGenderField(label="性别")
    age = serializers.SerializerMethodField(required=False, read_only=True, label="年龄")
    birthday = serializers.DateField(required=True, format="%Y-%m-%d", label="出生日期")
    create_time = serializers.DateTimeField(required=False, read_only=True, format="%Y-%d-%m %H:%M:%S", label="创建时间")
    update_time = serializers.DateTimeField(read_only=True, format="%Y-%d-%m %H:%M:%S", label="修改时间")

    def get_age(self, model: AuthorModel):
        today = datetime.today()
        return today.year - model.birthday.year - ((today.month, today.day) < (model.birthday.month, model.birthday.day))

    def validate_description(self, value):
        if value == "":
            return None
        return value

    def validate_birthday(self, value):
        if value > datetime.today().date():
            raise serializers.ValidationError("生日不能晚于当前日期")
        return value

    class Meta:
        model = AuthorModel
        exclude = ("status",)
        read_only_fields = ("age", "create_time", "update_time")
