from django.db.models.signals import post_save
from django.dispatch import receiver

from boards.models import Card, CheckList


@receiver(post_save, sender=Card)
def create_card_checklist(sender, instance=None, created=False, **kwargs):
    """
    This signal creates a CheckList instance and assign to the created
    Card.
    """

    if created:

        print("CheckList creado")

        CheckList.objects.create(
            name="Acceptance criteria",
            card=instance
        )