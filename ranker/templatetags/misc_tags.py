from django import template

from ranker.util import get_media_url

__author__ = 'shillaker'

register = template.Library()


@register.simple_tag
def media(filename):
    return get_media_url(filename)
