# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-08-04 15:45:26 UTC+08:00
"""

from django.db import models


class UserGroupModel(models.Model):
    pkid = models.AutoField(db_column="id", primary_key=True, verbose_name="ID")
    name = models.CharField(db_column="name", max_length=255, unique=True, verbose_name="用户组名")
    status = models.BooleanField(db_column="exist", default=True, verbose_name="数据状态")
    create_time = models.DateTimeField(db_column="created_at", auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(db_column="updated_at", auto_now=True, verbose_name="修改时间")

    class Meta:
        db_table = "public_dev_test\".\"user_group"
        verbose_name = "用户组"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserModel(models.Model):
    pkid = models.AutoField(db_column="id", primary_key=True, verbose_name="ID")
    username = models.CharField(db_column="username", max_length=255, unique=True, verbose_name="用户名")
    password = models.CharField(db_column="password", max_length=255, verbose_name="密码")
    email = models.EmailField(db_column="email", max_length=255, unique=True, verbose_name="邮箱地址")
    group_id = models.ForeignKey(
        db_column="group_id",
        related_name="group",
        null=True,
        blank=True,
        to="UserGroupModel",
        to_field="pkid",
        on_delete=models.SET_NULL,
        db_constraint=False,
        verbose_name="用户组ID",
    )
    status = models.BooleanField(db_column="exist", default=True, verbose_name="数据状态")
    create_time = models.DateTimeField(db_column="created_at", auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(db_column="updated_at", auto_now=True, verbose_name="修改时间")

    class Meta:
        db_table = "public_dev_test\".\"user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
