from rest_framework.routers import DefaultRouter
from main.views import OrderViewSet, ProductViewSet, CustomerViewSet

router = DefaultRouter()
router.register('customers', CustomerViewSet, basename='Customer')
router.register('orders', OrderViewSet, basename='Order')
router.register('products', ProductViewSet, basename='Product')
urlpatterns = router.urls