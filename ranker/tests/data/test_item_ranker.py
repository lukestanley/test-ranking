from django.test.testcases import TestCase

from ranker.data.item_ranker import rank_all_items
from ranker.models import Item
from ranker.tests.factories import ItemFactory, SellerFactory

__author__ = 'shillaker'


class ItemRankerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        super(ItemRankerTest, cls).setUpTestData()

        cls.seller_a = SellerFactory()

        cls.item_a = ItemFactory(seller=cls.seller_a)
        cls.item_b = ItemFactory(seller=cls.seller_a)

    def test_ranker_returns_all_items(self):
        n_items = Item.objects.all().count()

        actual_items = rank_all_items()

        self.assertEqual(n_items, len(actual_items))
