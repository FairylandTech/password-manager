# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-06 03:36:21 UTC+8
"""


class ApiResponse:

    def __init__(self, serializer_data):
        self.serizlizer_data = serializer_data

    @property
    def results(self):
        return {"status": "success", "code": 200, "data": self.serizlizer_data}
