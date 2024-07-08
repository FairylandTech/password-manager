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


_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
_DATE_FORMAT = "%Y-%m-%d"
_TIME_FORMAT = "%H:%M:%S"


class AuthorModelGenderChoices:
    choices = (("", ""), (0, "男"), (1, "女"))


class AuthorModelGenderField(serializers.ChoiceField):

    def to_representation(self, value):
        return "男" if value else "女"

    def to_internal_value(self, data):
        if data in ("男", 0, True, "0", "Ture", "true"):
            return True
        elif data in ("女", 1, False, "1", "False", "false"):
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

    id = serializers.IntegerField(required=False, read_only=True, label="ID")
    name = serializers.CharField(max_length=255, label="作者姓名")
    sex = AuthorModelGenderField(source="gender", choices=AuthorModelGenderChoices.choices, label="作者性别")
    age = serializers.SerializerMethodField(required=False, read_only=True, label="作者年龄")
    birthday = serializers.DateField(format=_DATE_FORMAT, label="作者出生日期")
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True, default=None, label="作者描述")
    create_time = serializers.DateTimeField(required=False, read_only=True, format=_DATETIME_FORMAT, label="创建时间")
    update_time = serializers.DateTimeField(read_only=True, format=_DATETIME_FORMAT, label="修改时间")

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

    def validate(self, attrs):
        return super().validate(attrs)

    class Meta:
        model = AuthorModel
        fields = ("id", "name", "sex", "age", "birthday", "description", "create_time", "update_time")
        # exclude = ("status", "gender")
