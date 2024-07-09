# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-15 15:12:04 UTC+8
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.example.views.test import Test
from apps.example.views.example import ExampleViewSet
from apps.example.views.generic import PublishViewSet, AuthorViewSet
from apps.example.views.generic import PublishAPIView, AuthorAPIView
from apps.example.views.generic import AuthorDetailAPIView
from apps.example.views.generic import PseudoCodeAPIViewSet

from apps.example.views.generic import SimpleUserGroupViewSet


router = DefaultRouter()
router.trailing_slash = ""
router.register(r"example", ExampleViewSet)
router.register(r"publish", PublishViewSet)
router.register(r"author", AuthorViewSet)
router.register(r"usergroup", SimpleUserGroupViewSet)

urlpatterns = [
    path(r"drf/", include(router.urls)),
    path(r"apiview", Test.as_view()),
    path(r"publish-apiview", PublishAPIView.as_view()),
    path(r"author-apiview", AuthorAPIView.as_view()),
    path(r"author-apiview/<int:pk>", AuthorDetailAPIView.as_view()),
    path(r"pseudo-code", PseudoCodeAPIViewSet.as_view({"get": "get_all", "post": "create_data"})),
    path(r"pseudo-code/<int:pk>", PseudoCodeAPIViewSet.as_view({"get": "get_data", "put": "update_data_all", "patch": "update_data_partial", "delete": "delete_data"})),
]
