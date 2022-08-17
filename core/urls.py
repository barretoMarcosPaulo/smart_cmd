from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommandsViewSet, DevicesViewSet, IntentsViewSet, ReceiveCommandViewSet

router = DefaultRouter()
router.register("devices", DevicesViewSet, basename="devices")
router.register("commands", CommandsViewSet, basename="commands")
router.register("intents", IntentsViewSet, basename="intents")

urlpatterns = [
    path("command-executation/", ReceiveCommandViewSet.as_view({"post": "create"})),
]

urlpatterns += router.urls
