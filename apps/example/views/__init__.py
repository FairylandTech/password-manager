# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-15 15:11:44 UTC+8
"""

from django.views import View
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ViewSet, GenericViewSet
# 和 `GenericViewSet` 配合使用的混合方法
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin

"""
1. 继承`View` 定义: `get`, `post`, `put`, `patch`, 'delete`
2. 继承`APIView` 定义: `get`, `post`, `put`, `patch`, 'delete`
    参数 `request` 是 rest_framework.request.Request
    返回 `response` 是 rest_framework.response.Response
3. 继承`ViewSet`
    - 在url中注明什么请求方式走 `ViewSet` 中的那个方法: <视图集>.as_view({"get": "<视图集中的方法名>", "post": "<视图集中的方法名>"})
    - 在 rest_framework.routers 中使用路由注册, 添加到 `urlpatterns` 中: 使用 `include` 也可以使用 `urlpatterns += router`
4. 继承`GenericViewSet`
    - 在url中注明什么请求方式走 `GenericViewSet` 中的那个方法: <视图集>.as_view({"get": "<视图集中的方法名>", "post": "<视图集中的方法名>"})
    - 在 rest_framework.routers 中使用路由注册, 添加到 `urlpatterns` 中: 使用 `include` 也可以使用 `urlpatterns += router`
"""
