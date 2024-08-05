# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-08-04 23:12:51 UTC+08:00
"""

from datetime import datetime
from datetime import timezone
from datetime import timedelta


class DatetimeUtil:
    zonename = "Asia/Shanghai"

    @classmethod
    def current_beijing(cls):
        return datetime.now(cls.zone())

    @classmethod
    def zone(cls):
        return timezone(timedelta(hours=8), cls.zonename)
