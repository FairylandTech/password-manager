# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-14 23:45:54 UTC+8
"""


class ProgramError(Exception):

    def __init__(self, message: str = "Internal program error."):
        self.prompt = f"{self.__class__.__name__}: {message}"

    def __str__(self) -> str:
        return self.prompt


class DataSourceError(ProgramError):

    def __init__(self, message: str = "Data source error."):
        self.prompt = f"{self.__class__.__name__}: {message}"

    def __str__(self):
        return self.prompt


class CacheError(ProgramError):

    def __init__(self, message: str = "Cache error."):
        self.prompt = f"{self.__class__.__name__}: {message}"

    def __str__(self):
        return self.prompt


class RequestParametersMissing(ProgramError):

    def __init__(self, message: str = "Request parameters missing."):
        self.message = message
        self.prompt = f"{self.__class__.__name__}: {message}"

    def __str__(self):
        return self.prompt
