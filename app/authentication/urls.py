from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .api import MemberViewSet, LoginView


router = DefaultRouter()
router.register("members", MemberViewSet)

urlpatterns = [
    path("login/", LoginView.as_view()),

    path("", include(router.urls)),
]
