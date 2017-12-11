from rest_framework.serializers import ModelSerializer

from boards.models import Board, Card, CheckList, CheckItem


class CardSerializer(ModelSerializer):
    """
    Serializer for Card model.
    """

    class Meta:
        model = Card
        fields = ['id', 'name', 'assigned', 'created', 'modified']


class BoardSerializer(ModelSerializer):
    """
    Serializer for Board model.
    """

    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ['id', 'cards', 'created', 'modified']