from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .api import BlogViewSet


router = DefaultRouter()
router.register("blogs", BlogViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
