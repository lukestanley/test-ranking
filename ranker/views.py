from django.views.generic.base import TemplateView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ranker.data.item_ranker import rank_all_items
from ranker.serializers import ItemSerializer


__author__ = 'shillaker'


class MainView(TemplateView):
    template_name = 'ranker.html'


class ItemViewSet(ViewSet):
    def list(self, request):
        items = rank_all_items()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
