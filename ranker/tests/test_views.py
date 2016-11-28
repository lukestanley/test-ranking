from json import loads

from django.test.testcases import TestCase
from django.urls.base import reverse

from ranker.tests.factories import ItemFactory, SellerFactory

__author__ = 'shillaker'


class ItemsApiViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        super(ItemsApiViewTest, cls).setUpTestData()

        cls.seller_a = SellerFactory()

        cls.item_a = ItemFactory(seller=cls.seller_a)
        cls.item_b = ItemFactory(seller=cls.seller_a)

    def test_json_view_returns_all_items(self):
        response = self.client.get(reverse('item-list'))
        self.assertEqual(200, response.status_code)

        actual = loads(response.content)
        self.assertEqual(2, len(actual['results']))
