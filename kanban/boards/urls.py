from rest_framework.routers import SimpleRouter

from boards import views


router = SimpleRouter()

router.register('boards', views.BoardViewSet)
router.register('cards', views.CardViewSet)