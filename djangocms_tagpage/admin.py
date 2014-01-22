"""
@file   admin.py
@brief  To make this accessible in backend
"""

from django.contrib import admin
from cms.extensions import PageExtensionAdmin
from .models import PageTags

class PageTagsAdmin(PageExtensionAdmin):
    list_display = ['extended_object']

    def is_draft_page(self, page):
        return page.extended_object.publisher_is_draft

admin.site.register(PageTags, PageTagsAdmin)
