"""
@file   urls.py
"""

# Django imports
from django.conf.urls import patterns, url
# app imports
from .import views

urlpatterns = patterns('',
    url(r'^$', views.tag_overview, name='tag_overview'),
    url(r'^(?P<tag_name>\w+)/$', views.tag_detail, name='tag_detail'),
)
