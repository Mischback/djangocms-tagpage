"""
@file   models.py
@brief  Contains the necessary models
"""

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from taggit.managers import TaggableManager

class PageTags(PageExtension):
    tags = TaggableManager()

extension_pool.register(PageTags)
