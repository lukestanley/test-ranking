from ranker.models import Item

__author__ = 'shillaker'


def rank_all_items():
    items = list(Item.objects.all())
    def view_and_wish_sort(i):
        total_item_views = i.itemview_set.count()
        total_wish_list_entries = i.wishlistentry_set.count()
        item_popularity_score = total_item_views + (2 * total_wish_list_entries)
        return item_popularity_score
    items = sorted(items, key=view_and_wish_sort)
    
    return items

"""
items = Item.objects.all()

for item in items:
    print(item)"""
