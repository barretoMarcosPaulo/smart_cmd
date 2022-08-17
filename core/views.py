from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.views.generic import TemplateView
from rest_framework import status, viewsets
from rest_framework.response import Response

from core.models import Commands, Devices, Intents

from .serializers import CommandsSerializer, DevicesSerializer, IntentsSerializer, ReceiveCommandSerializer


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


class DevicesViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer


class CommandsViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Commands.objects.all()
    serializer_class = CommandsSerializer


class IntentsViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Intents.objects.all()
    serializer_class = IntentsSerializer
