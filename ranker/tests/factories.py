from factory.declarations import SubFactory
from factory.django import DjangoModelFactory

from ranker.models import Item, Seller, ItemView, WishListEntry, WishList


class SellerFactory(DjangoModelFactory):
    class Meta:
        model = Seller


class ItemFactory(DjangoModelFactory):
    class Meta:
        model = Item

    seller = SubFactory(SellerFactory)


class ItemViewFactory(DjangoModelFactory):
    class Meta:
        model = ItemView

    item = SubFactory(ItemFactory)


class WishListFactory(DjangoModelFactory):
    class Meta:
        model = WishList


class WishListEntryFactory(DjangoModelFactory):
    class Meta:
        model = WishListEntry

    item = SubFactory(ItemFactory)
    wish_list = SubFactory(WishListFactory)
