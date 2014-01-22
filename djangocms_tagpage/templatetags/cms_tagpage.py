"""
@file   cms_tagpage.py
"""

# Django imports
from django import template

register = template.Library()

@register.assignment_tag(takes_context=True):
def get_tags(context):
    """
    @brief  Fetches Tag objects
    """
    # get all available tags
    tags = Tag.objects.all()

    return tags
