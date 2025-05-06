from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaisViewSet, ProvinciaViewSet, CiudadViewSet

router = DefaultRouter()
router.register(r'paises', PaisViewSet)
router.register(r'provincias', ProvinciaViewSet)
router.register(r'ciudades', CiudadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
