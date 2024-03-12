from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

from .views import (
    ConsumablesViewSet,
    CustomersViewSet,
    OrderDetailsViewSet,
    OrdersViewSet,
    ServicesViewSet,
)

router = DefaultRouter()
router.register(r'consumables', ConsumablesViewSet)
router.register(r'customers', CustomersViewSet)
router.register(r'order-details', OrderDetailsViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'services', ServicesViewSet)
# Create a schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Dr Na API",
        default_version='v1',
        description="Clinic Management",
        terms_of_service="wequip.vn/drna",
        contact=openapi.Contact(email="contact@example.com"),
    ),
    public=True,
)

urlpatterns = [
    # API
    path('api/', include(router.urls)),

    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # ReDoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
