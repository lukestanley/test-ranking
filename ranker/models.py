from django.db.models.base import Model
from django.db.models.fields import CharField, DateTimeField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

from ranker.util import datetime_now

__author__ = 'shillaker'


class Seller(Model):
    name = CharField(max_length=20)


class Item(Model):
    seller = ForeignKey(Seller)
    name = CharField(max_length=30)
    image = ImageField(null=True, blank=True)
    image_b = ImageField(null=True, blank=True)
    image_c = ImageField(null=True, blank=True)
    image_d = ImageField(null=True, blank=True)


class ItemView(Model):
    item = ForeignKey(Item)
    date = DateTimeField(default=datetime_now)


class WishList(Model):
    name = CharField(max_length=20)


class WishListEntry(Model):
    item = ForeignKey(Item)
    wish_list = ForeignKey(WishList)
    date = DateTimeField(default=datetime_now)
