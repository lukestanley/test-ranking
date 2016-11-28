from django.core.management.base import BaseCommand

from ranker.data.data_populator import populate_item_data


class Command(BaseCommand):
    help = 'Populates the dummy ranking data'

    def handle(self, *args, **kwargs):
        populate_item_data()
