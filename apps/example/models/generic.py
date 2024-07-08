# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-06 23:26:43 UTC+8
"""

from django.db import models


class PublishModel(models.Model):

    name = models.CharField(db_column="name", max_length=255, unique=True, verbose_name="出版社名字")
    ares = models.CharField(db_column="area", max_length=255, verbose_name="出版社地区")
    status = models.BooleanField(db_column="exist", default=True, blank=True, verbose_name="数据状态")
    create_time = models.DateTimeField(db_column="created_at", auto_now_add=True, blank=True, verbose_name="创建时间")
    update_time = models.DateTimeField(db_column="updated_at", auto_now=True, verbose_name="修改时间")

    class Meta:
        db_table = 'public_dev_test"."pubilsh'
        verbose_name = "出版社"
        verbose_name_plural = verbose_name


class AuthorModel(models.Model):

    name = models.CharField(db_column="name", max_length=255, verbose_name="作者姓名")
    gender = models.BooleanField(db_column="gender", verbose_name="作者性别", choices=((True, "男"), (False, "女")))  # true=1=男, false=0=女
    birthday = models.DateField(db_column="birthday", verbose_name="作者出生日期")
    description = models.TextField(db_column="description", null=True, default=None, blank=True, verbose_name="作者描述")
    status = models.BooleanField(db_column="exist", default=True, verbose_name="数据状态")
    create_time = models.DateTimeField(db_column="created_at", auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(db_column="updated_at", auto_now=True, verbose_name="修改时间")

    class Meta:
        db_table = 'public_dev_test"."author'
        verbose_name = "作者"
        verbose_name_plural = verbose_name
