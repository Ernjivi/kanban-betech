from django.contrib import admin

from profiles.models import Profile

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    """
    Model admin for profile model.
    """
    pass