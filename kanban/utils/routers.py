from rest_framework import routers


class DefaultRouter(routers.DefaultRouter):
    """
    Extends 'DefaultRouter' class to add a method for extending url routes form
    another applications.
    """

    def extend(self, router):
        self.registry.extend(router.registry)