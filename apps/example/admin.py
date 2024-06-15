from django.contrib import admin

# Register your models here.

from .models.example import Example

admin.site.register(Example)
