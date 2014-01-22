"""
@file   cms_toolbar.py
@brief  Make this accessible in toolbar

DjangoCMS 3 makes great use of "frontend editing", which means, that most of
the changes can be made without using the actual administration backend of
Django.

The CMSToolbar is the tool for this frontline editing.

This file provides the means to edit Tags from the toolbar.
"""

# Django imports
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.translation import ugettext_lazy as _
# DjangoCMS imports
from cms.api import get_page_draft
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
# app imports
from .models import PageTags

@toolbar_pool.register
class PageTagsToolbar(CMSToolbar):
    """
    @class  PageTagsToolbar
    @brief  Modifies/enhances the CMSToolbar object
    """
    def populate(self):
        """
        @brief  This method actually makes the modifications to the toolbar
        """
        # all changes will be made on the draft version of the page
        self.page = get_page_draft(self.request.current_page)

        if not self.page:
            # if there is no page, there is nothing to do...
            return

        try:
            # fetch existing PageTags-object
            page_tags = PageTags.objects.get(extended_object_id=self.page.id)
        except PageTags.DoesNotExist:
            # this page has not been tagged yet!
            page_tags = None

        try:
            if page_tags:
                # if we have existing tags, use modification dialogue
                url = reverse('admin:djangocms_tagpage_pagetags_change',
                    args=(page_tags.pk,))
            else:
                # use initial creation dialogue
                url = reverse(
                    'admin:djangocms_tagpage_pagetags_add'
                    ) + '?extended_object={0}'.format(self.page.pk)
        except NoReverseMatch:
            # if no URL could be fetched, fail silently
            pas
        else:
            # Add our own menu entry to the toolbar (as child of 'page')
            not_edit_mode = not self.toolbar.edit_mode
            current_page_menu = self.toolbar.get_or_create_menu('page')
            current_page_menu.add_modal_item(_('Tags'),
                url=url,
                disabled=not_edit_mode)
