from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AddCommand,
    AddDevice,
    AddIntent,
    CommandsViewSet,
    Dashboard,
    DevicesViewSet,
    IntentsViewSet,
    ListCommands,
    ListDevices,
    ListIntent,
    ReceiveCommandViewSet,
)

router = DefaultRouter()
router.register("devices", DevicesViewSet, basename="devices")
router.register("commands", CommandsViewSet, basename="commands")
router.register("intents", IntentsViewSet, basename="intents")

urlpatterns = [
    path("command-executation/", ReceiveCommandViewSet.as_view({"post": "create"})),
    path("", Dashboard.as_view(), name="home"),
    path("device-add", AddDevice.as_view(), name="device_add"),
    path("device-list", ListDevices.as_view(), name="list_devices"),
    path("command-add", AddCommand.as_view(), name="command_add"),
    path("command-list", ListCommands.as_view(), name="list_commands"),
    path("intent-add", AddIntent.as_view(), name="intent_add"),
    path("intent-list", ListIntent.as_view(), name="intent_list"),
]

# urlpatterns += router.urls
