# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-15 10:06:46 UTC+8
"""

import pymysql

from django.conf import settings


class DataSourceBin:

    @classmethod
    def process(cls):
        data_source_config = settings.DATA_SOURCE_CONFIG

        db_name = data_source_config.get("database")
        conn = pymysql.connect(
            host=data_source_config.get("host"),
            user=data_source_config.get("username"),
            password=data_source_config.get("password"),
            port=data_source_config.get("port"),
            charset=data_source_config.get("charset"),
            cursorclass=pymysql.cursors.DictCursor,
        )

        try:
            with conn.cursor() as cursor:
                cursor.execute(f"create database if not exists {db_name} default character set utf8mb4 collate utf8mb4_unicode_ci;")
        finally:
            conn.close()
            
        from django.core.cache import cache
        from django_redis import get_redis_connection
        
        
