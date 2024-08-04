# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-08-04 15:49:57 UTC+08:00
"""

from django.db import models


class PublishModel(models.Model):
    name = models.CharField(db_column="name", max_length=255, unique=True, verbose_name="出版社名字")
    area = models.CharField(db_column="area", max_length=255, blank=True, null=True, verbose_name="出版社地区")
    status = models.BooleanField(db_column="existed", default=True, verbose_name="数据状态")
    create_time = models.DateTimeField(db_column="created", auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(db_column="updated", auto_now=True, verbose_name="修改时间")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "public_dev_test\".\"publish"
        ordering = ("update_time", "pk")
        verbose_name = "出版社表"
        verbose_name_plural = verbose_name


class AuthorModel(models.Model):
    name = models.CharField(db_column="name", max_length=255, verbose_name="作者姓名")
    gender = models.BooleanField(db_column="gender", verbose_name="作者性别", choices=((True, "男"), (False, "女")))
    birthday = models.DateField(db_column="birthday", verbose_name="作者出生日期")
    description = models.TextField(db_column="description", blank=True, null=True, verbose_name="作者描述")
    status = models.BooleanField(db_column="existed", default=True, verbose_name="数据状态")
    create_time = models.DateTimeField(db_column="created", auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(db_column="updated", auto_now=True, verbose_name="修改时间")

    class Meta:
        db_table = "public_dev_test\".\"author"
        ordering = ("name", "pk", "update_time")
        verbose_name = "作者表"
        verbose_name_plural = verbose_name
