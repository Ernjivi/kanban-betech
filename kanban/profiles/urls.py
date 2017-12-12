from rest_framework.routers import SimpleRouter

from profiles.views import UserViewSet


router = SimpleRouter()
router.register('users', UserViewSet)