from rest_framework.viewsets import ModelViewSet

from boards.models import Board, Card, CheckList, CheckItem
from boards.serializers import (
    BoardSerializer,
    CardSerializer,
    CheckListSerializer,
    CheckItemSerializer,
)


class BoardViewSet(ModelViewSet):
    """
    List, retrieve, add, update instances of Board model.
    """

    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class CardViewSet(ModelViewSet):
    """
    List, retieve, add, update instances of Card model.
    """

    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CheckListViewSet(ModelViewSet):
    """
    List, retrieve, add, update instances of CheckList model.
    """

    queryset = CheckList.objects.all()
    serializer_class = CheckListSerializer


class CheckItemViewSet(ModelViewSet):
    """
    List, retriebe, add, update instances of CheckItem model.
    """

    queryset = CheckItem
    serializer_class = CheckItemSerializer