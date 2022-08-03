from django.urls import path

from .views import ReceiveCommandViewSet

urlpatterns = [
    path("command/", ReceiveCommandViewSet.as_view({"post": "create"})),
]
