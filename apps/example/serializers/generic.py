# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-06 23:45:52 UTC+8
"""

from datetime import datetime, timezone, timedelta

from rest_framework import serializers

from apps.example.models.generic import PublishModel, AuthorModel
from apps.example.models.generic import UserGroupModel, UserModel

from utils.journal import journal


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

    def get_age(self, instance: AuthorModel):
        today = datetime.today()
        return today.year - instance.birthday.year - ((today.month, today.day) < (instance.birthday.month, instance.birthday.day))

    def validate_description(self, value):
        if value == "":
            return None
        return value

    def validate_birthday(self, value):
        if value > datetime.today().date():
            raise serializers.ValidationError("不能晚于当前日期")
        return value

    def validate(self, attrs):
        return super().validate(attrs)

    class Meta:
        model = AuthorModel
        fields = ("id", "name", "sex", "age", "birthday", "description", "create_time", "update_time")
        # exclude = ("status", "gender")


class UserGroupModelSerializer(serializers.ModelSerializer):

    _DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    id = serializers.IntegerField(source="pkid", required=False, read_only=True, label="ID")
    name = serializers.CharField(max_length=255, label="用户组名")
    create_time = serializers.DateTimeField(required=False, read_only=True, format=_DATETIME_FORMAT, label="创建时间")
    update_time = serializers.DateTimeField(required=False, read_only=True, format=_DATETIME_FORMAT, label="修改时间")

    class Meta:
        model = UserGroupModel
        fields = ["id", "name", "create_time", "update_time"]

    def validate_name(self, value):
        if UserGroupModel.objects.filter(name=value).exists():
            raise serializers.ValidationError("This name already exists.")
        return value

    def create(self, validated_data):
        journal.debug(f"Create >>> validated data: {validated_data}, type is {type(validated_data)}")
        if "create_time" not in validated_data:
            validated_data.update(create_time=datetime.now(tz=timezone(timedelta(hours=8), name="Asia/Shanghai")))
        if "update_time" not in validated_data:
            validated_data.update(update_time=datetime.now(tz=timezone(timedelta(hours=8), name="Asia/Shanghai")))

        return super().create(validated_data)

    def update(self, instance, validated_data):
        journal.debug(f"Update >>> validated data: {validated_data}, type is {type(validated_data)}")
        validated_data.update(update_time=datetime.now(tz=timezone(timedelta(hours=8), name="Asia/Shanghai")))

        return super().update(instance, validated_data)


class UserModelSerializer(serializers.ModelSerializer):

    _DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    id = serializers.IntegerField(source="pkid", required=False, read_only=True, label="ID")
    username = serializers.CharField(max_length=255, label="用户名")
    password = serializers.CharField(max_length=255, label="密码")
    email = serializers.EmailField(max_length=255, label="邮箱地址")
    group_id = serializers.IntegerField(source="group.pkid", required=False, label="用户组ID")
    group = serializers.CharField(source="group.name", required=False, read_only=True, label="用户组")
    create_time = serializers.DateTimeField(required=False, read_only=True, format=_DATETIME_FORMAT, label="创建时间")
    update_time = serializers.DateTimeField(required=False, read_only=True, format=_DATETIME_FORMAT, label="修改时间")

    class Meta:
        model = UserModel
        fields = ("id", "username", "password", "email", "create_time", "update_time", "group_id", "group")

    def validate_username(self, value):
        if UserModel.objects.filter(username=value).exists():
            raise serializers.ValidationError("重复用户名")
        return value

    def validate_email(self, value):
        if UserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError("重复邮箱")
        return value

    def validate_group_id(self, value):
        if not UserGroupModel.objects.filter(pkid=value).exists():
            raise serializers.ValidationError("没有组")
        return value

    def create(self, validated_data):
        # POST -> form-data : validated_data 是 dict
        # POST -> application/json : validated_data 是 dict
        # POST -> application/x-www-form-urlencoded : validated_data 是 dict
        journal.debug(f"Create >>> validated data: {validated_data}, type is {type(validated_data)}")
        if "create_time" not in validated_data:
            validated_data.update(create_time=datetime.now(tz=timezone(timedelta(hours=8), name="Asia/Shanghai")))
        if "update_time" not in validated_data:
            validated_data.update(update_time=datetime.now(tz=timezone(timedelta(hours=8), name="Asia/Shanghai")))

        return super().create(validated_data)

    def update(self, instance, validated_data):
        journal.debug(f"Update >>> validated data: {validated_data}, type is {type(validated_data)}")
        validated_data.update(update_time=datetime.now(tz=timezone(timedelta(hours=8), name="Asia/Shanghai")))

        return super().update(instance, validated_data)
