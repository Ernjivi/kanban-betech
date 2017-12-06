from django.db import models
from django.conf import settings


class Board(models.Model):
    """
    Board model.
    """

    name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="boards")
    colaborators = models.ManyToManyField(settings.AUTH_USER_MODEL)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    """
    Board card model.
    """

    board = models.ForeignKey(Board, related_name='cards')
    name = models.CharField(max_length=255)
    assigned = models.ManyToManyField(settings.AUTH_USER_MODEL)
    due_date = models.DateTimeField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CheckList(models.Model):
    """
    Check list model for cards
    """

    card = models.ForeignKey(Card)
    name = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CheckItem(models.Model):
    """
    Check Item in check list model.
    """

    text = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text