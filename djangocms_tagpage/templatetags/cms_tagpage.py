"""
@file   cms_tagpage.py
"""

# Django imports
from django import template
# external app imports
from taggit.models import Tag, TaggedItem

register = template.Library()

@register.assignment_tag(takes_context=True)
def get_tags(context):
    """
    @brief  Fetches Tag objects
    """
    # get all available tags
    tags = Tag.objects.all()

    # just return the tags in use
    # @todo: Make this configurable?!
    used_tags = TaggedItem.objects.all().values_list('tag_id', flat=True)
    tags = tags.filter(id__in=used_tags)

    return tags
