from django.conf import settings
from django.db import models



class Profile(models.Model):
    """
    Holds information about a user.
    """

    MALE_CHOICE = 1
    FEMALE_CHOICE = 2
    OTHER_CHOICE = 3

    GENDER_CHOICES = (
        (MALE_CHOICE, 'Male'),
        (FEMALE_CHOICE, 'Female'),
        (OTHER_CHOICE, 'Not specified')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, default=OTHER_CHOICE)

    def __str__(self):

        return '%s\'s profile' % self.user.get_username()