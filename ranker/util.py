from datetime import datetime

from django.conf.global_settings import MEDIA_URL
from pytz import UTC

__author__ = 'shillaker'


def datetime_now():
    now = datetime.utcnow().replace(tzinfo=UTC)
    return now


def get_media_url(filename):
    media_url = '%s%s' % (MEDIA_URL, '' if MEDIA_URL.endswith('/') else '/')

    if filename is not None and filename.startswith('/'):
        filename = filename[1:]

    return '%s%s' % (media_url, filename)
