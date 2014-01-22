"""
@file   views.py
"""

# Django imports
from django.shortcuts import render

def tag_overview(request):
    return render(request, 'tag_overview.html')

def tag_detail(request, tag_name):
    return render(request, 'tag_detail.html', {'tag_name': tag_name})
