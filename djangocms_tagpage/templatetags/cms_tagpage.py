"""
@file   cms_tagpage.py
"""

# Django imports
from django import template
# DjangoCMS imports
from cms.api import get_page_draft
# external app imports
from taggit.models import Tag, TaggedItem
# app imports
from djangocms_tagpage.models import PageTags

register = template.Library()

@register.assignment_tag(takes_context=True)
def get_tags(context, limit=None):
    """
    @brief  Fetches Tag objects
    """
    tagged_items = None
    # get all available tags
    tags = Tag.objects.all()

    if 'page' == limit:
        # just return tags of the current page...
        # get the ID of the current page's draft version (all changes are made
        # to the draft version in DjangoCMS)
        current_page = get_page_draft(context['request'].current_page).id
        try:
            # find the matching PageTags object's id
            pagetags_id = PageTags.objects.get(extended_object_id=current_page).id
            # get all TaggedItems associated with this PageTags object
            tagged_items = TaggedItem.objects.filter(object_id=pagetags_id)
        except PageTags.DoesNotExist:
            # obviously this page is not tagged, so there are no tagged items
            tagged_items = None

    if not tagged_items:
        # just return the tags in use
        # @todo: Make this configurable?!
        tagged_items = TaggedItem.objects.all().values_list('tag_id', flat=True)

    tags = tags.filter(id__in=tagged_items)

    return tags
