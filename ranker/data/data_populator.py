from datetime import timedelta
from os.path import dirname, abspath, join
from random import randint

from django.core.files.base import File
from numpy.random import normal

from ranker.models import Item, ItemView, Seller, WishListEntry, WishList
from ranker.util import datetime_now

__author__ = 'shillaker'


def populate_item_data():
    WishListEntry.objects.all().delete()
    WishList.objects.all().delete()
    ItemView.objects.all().delete()
    Item.objects.all().delete()
    Seller.objects.all().delete()

    print 'Inserting sellers'
    _insert_sellers()
    print 'Inserting items'
    _insert_items()
    print 'Inserting item views'
    _insert_item_views()
    print 'Inserting wish lists'
    _insert_wish_lists()
    print 'Inserting wish list items'
    _insert_wishlist_items()


def _insert_sellers():
    sellers = list()
    for i in range(0, 5):
        sellers.append(Seller(name='Seller %d' % i))

    Seller.objects.bulk_create(sellers)


def _insert_items():
    sellers = Seller.objects.all()

    for i in range(0, 20):
        seller = _sample_list(sellers)
        item = Item(name='Item %d' % i, seller=seller)
        item.save()

        item.image.save(*_get_random_image_path())
        item.image_b.save(*_get_random_image_path())
        item.image_c.save(*_get_random_image_path())
        item.image_d.save(*_get_random_image_path())


def _insert_wish_lists():
    for i in range(0, 20):
        wish_list = WishList(name='List %d' % i)
        wish_list.save()


def _get_random_image_path():
    proj_dir = dirname(dirname(abspath(__file__)))

    img_num = randint(1, 5)
    image_file = 'image_%d.jpg' % img_num
    image_path = join(proj_dir, 'images', image_file)

    img_file = File(open(image_path))

    return image_file, img_file


def _insert_item_views():
    items = list(Item.objects.all())

    views = list()
    for i in range(0, 500):
        item = _sample_list(items)
        this_dt = datetime_now() - timedelta(days=randint(0, 100))
        views.append(ItemView(item=item, date=this_dt))

    ItemView.objects.bulk_create(views)


def _insert_wishlist_items():
    items = list(Item.objects.all())
    wish_lists = list(WishList.objects.all())

    entries = list()
    for i in range(0, 100):
        wish_list = _sample_list(wish_lists)
        item = _sample_list(items)
        entries.append(WishListEntry(item=item, wish_list=wish_list))

    WishListEntry.objects.bulk_create(entries)


def _sample_list(list_in):
    n_elements = len(list_in)

    # Work out suitably narrow stddev
    sigma = int(n_elements / 10)
    sigma = max(sigma, 1)

    # Sample normal distribution
    idx = normal(n_elements / 2, sigma, 1)[0]
    idx = int(idx)

    # Floor/ ceiling
    idx = max(idx, 0)
    idx = min(idx, n_elements - 1)

    return list_in[idx]
