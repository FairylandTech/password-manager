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

from apps.example.views.example import ExampleViewSet

router = DefaultRouter()
router.register(r"test", ExampleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
