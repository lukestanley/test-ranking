from django.views.generic.base import TemplateView
from rest_framework.viewsets import ModelViewSet

from ranker.data.item_ranker import rank_all_items
from ranker.serializers import ItemSerializer

__author__ = 'shillaker'


class MainView(TemplateView):
    template_name = 'ranker.html'


class ItemViewSet(ModelViewSet):
    queryset = rank_all_items()
    serializer_class = ItemSerializer
