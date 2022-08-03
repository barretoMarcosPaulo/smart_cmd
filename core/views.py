import threading

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.views.generic import TemplateView
from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializers import ReceiveCommandSerializer


class DashboardView(TemplateView):
    template_name = "dashboard.html"


class ReceiveCommandViewSet(viewsets.ModelViewSet):
    serializer_classes = {
        "create": ReceiveCommandSerializer,
    }

    def create(self, request, *args, **kwargs):
        data = self.request.data
        serializer = self.serializer_classes["create"](data=data)
        serializer.is_valid(raise_exception=True)

        layer = get_channel_layer()
        async_to_sync(layer.group_send)("teste", {"type": "receive_message", "command": data["action"]})

        return Response({}, status=status.HTTP_201_CREATED)
