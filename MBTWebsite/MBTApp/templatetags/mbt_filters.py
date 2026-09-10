"""Custom template filters/filters used across MBT templates.

Loaded with `{% load mbt_filters %}`.
"""
from django import template

register = template.Library()


@register.filter(name='get_item')
def get_item(d, key):
    """Dict lookup: {{ mydict|get_item:key }} -> value or ''."""
    if isinstance(d, dict):
        return d.get(key, '')
    return ''
