from rest_framework.serializers import ModelSerializer

from boards.models import Board, Card, CheckList, CheckItem

class CheckItemSerializer(ModelSerializer):
    """
    Serializer for CheckItem model.
    """

    class Meta:
        model = CheckItem
        fields = ['id', 'text', 'status']


class CheckListSerializer(ModelSerializer):
    """
    Serializer for CheckList model.
    """

    checks = CheckItemSerializer(many=True, read_only=True)

    class Meta:
        model = CheckList
        fields = ['name', 'checks']


class CardSerializer(ModelSerializer):
    """
    Serializer for Card model.
    """

    check_lists = CheckListSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        fields = ['id', 'name', 'board', 'check_lists']


class BoardSerializer(ModelSerializer):
    """
    Serializer for Board model.
    """

    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ['id', 'name', 'cards', 'created', 'modified']