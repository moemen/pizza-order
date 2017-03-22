from rest_framework import routers
from .views import OrderViewset

router = routers.SimpleRouter()
router.register(r'orders', OrderViewset)

urlpatterns = router.urls
