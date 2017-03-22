from rest_framework import routers
from .views import PizzaViewset

router = routers.SimpleRouter()
router.register(r'pizza', PizzaViewset)

urlpatterns = router.urls
