from rest_framework import routers
from .api import CustomersViewSet

router = routers.DefaultRouter()
router.register('api/customers', CustomersViewSet, 'customers')

urlpatterns = router.urls 