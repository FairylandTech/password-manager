# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-06 03:36:21 UTC+8
"""

from rest_framework import status


class APIResults:

    @staticmethod
    def success(data, code=status.HTTP_200_OK, message="success"):
        return {"status": "success", "code": code, "data": data, "message": message}

    @staticmethod
    def error(message, code=status.HTTP_400_BAD_REQUEST):
        return {"status": "error", "code": code, "data": None, "message": message}

    @staticmethod
    def redirect(url):
        return {"status": "redirect", "code": status.HTTP_302_FOUND, "url": url}

    @staticmethod
    def redirect_to_detail(url):
        return {"detail": "Redirecting...", "Location": url}
