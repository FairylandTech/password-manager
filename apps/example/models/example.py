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
    
    name = models.CharField(max_length=64)
    email = models.EmailField()
    
    class Meta:
        db_table = "apps_example_example"
