"""
@file   cms_app.py
"""

# Django imports
from django.utils.translation import ugettext_lazy as _
# DjangoCMS imports
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class PageTagsApp(CMSApp):
    name = _('PageTags App')
    urls = ['djangocms_tagpage.urls']

# register in DjangoCMS
apphook_pool.register(PageTagsApp)
