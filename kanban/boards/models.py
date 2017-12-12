from django.db import models
from django.conf import settings


class Board(models.Model):
    """
    Board model.
    """

    name = models.CharField(max_length=255)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    """
    Board card model.
    """

    STATUS_BACKLOG = 0
    STATUS_FREEZER = 1
    STATUS_TODO = 2
    STATUS_ON_GOING = 3
    STATUS_TEST = 4
    STATUS_DONE = 5

    STATUS_CHOICES = (
        (STATUS_BACKLOG, 'Backlog'),
        (STATUS_FREEZER, 'Freezer'),
        (STATUS_TODO, 'To-Do'),
        (STATUS_ON_GOING, 'On going'),
        (STATUS_TEST, 'Test'),
        (STATUS_DONE, 'Done'),
    )

    board = models.ForeignKey(Board, related_name='cards')
    name = models.CharField(max_length=255)
    satatus = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=STATUS_BACKLOG)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CheckList(models.Model):
    """
    Check list model for cards
    """

    card = models.ForeignKey(Card, related_name='check_lists')
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