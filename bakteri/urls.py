from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BakteriViewSet, KategoriViewSet

router = DefaultRouter()
router.register(r'bakteri', BakteriViewSet)
router.register(r'kategori', KategoriViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
