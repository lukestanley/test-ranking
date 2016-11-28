from rest_framework.serializers import ModelSerializer

from ranker.models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ('name',)
