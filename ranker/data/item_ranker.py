from ranker.models import Item

__author__ = 'shillaker'


def rank_all_items():
    items = Item.objects.order_by('name')

    return items
