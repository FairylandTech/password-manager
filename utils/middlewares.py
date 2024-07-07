# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-07 15:11:40 UTC+8
"""

from django.http.request import HttpRequest

from utils.journal import journal


class SplitRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        journal.info(f" 🚀Request Start ::: method: {request.method}; path: {request.path} ".center(100, "="))
        
        response = self.get_response(request)

        return response
