# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-15 15:38:10 UTC+8
"""

from django.db import models


class Example(models.Model):

    name = models.CharField(db_column="name", max_length=255, verbose_name="姓名")
    age = models.IntegerField(db_column="age", verbose_name="年龄")
    email = models.EmailField(db_column="email", max_length=255, verbose_name="邮箱")
    description = models.TextField(db_column="description", verbose_name="描述")
    create_time = models.DateTimeField(db_column="created_at", auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(db_column="updated_at", auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "public_dev_password_manager\".\"test_using"
        # db_table = "test_using"
        verbose_name = "测试表"
        verbose_name_plural = verbose_name
