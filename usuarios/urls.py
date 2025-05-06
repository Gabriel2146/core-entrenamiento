from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerfilDeportistaViewSet

router = DefaultRouter()
router.register(r'perfiles', PerfilDeportistaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
