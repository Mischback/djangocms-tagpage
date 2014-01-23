"""
@file   models.py
@brief  Contains the necessary models

DjangoCMS provides a special PageExtension class, to add additional fields to
the Page model without "real" modifications of the DjangoCMS core.

The necessary model is in this file.
"""

# DjangoCMS imports
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
# external app imports
from taggit.managers import TaggableManager

class PageTags(PageExtension):
    """
    @class  PageTags
    @brief  This class defines an extension to pages

    This is the connector between the cms' page model and the taggit app.
    """
    tags = TaggableManager()

# register the extension in the cms
extension_pool.register(PageTags)
