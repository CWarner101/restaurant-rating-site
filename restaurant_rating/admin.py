"""
Connor Warner
CIS 218
2/28/24
"""

from django.contrib import admin

from .models import Review, Restaurant

admin.site.register(Review)
admin.site.register(Restaurant)
