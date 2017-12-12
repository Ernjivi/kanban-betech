from utils.routers import DefaultRouter

from profiles.urls import router as profiles_router
from boards.urls import router as boards_router


router = DefaultRouter()

router.extend(profiles_router)
router.extend(boards_router)

urlpatterns = router.urls