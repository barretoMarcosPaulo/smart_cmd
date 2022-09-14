from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import redirect
from django.views.generic import TemplateView
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import Commands, Devices, Intents, ExecutionIntentsLogs
from datetime import datetime
from .serializers import CommandsSerializer, DevicesSerializer, IntentsSerializer, ReceiveCommandSerializer
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required


class ReceiveCommandViewSet(viewsets.ModelViewSet):
    serializer_classes = {
        "create": ReceiveCommandSerializer,
    }

    def create(self, request, *args, **kwargs):
        data = self.request.data
        serializer = self.serializer_classes["create"](data=data)
        serializer.is_valid(raise_exception=True)

        intent = Intents.objects.filter(name=data["action"]).first()

        if intent:
            layer = get_channel_layer()
            async_to_sync(layer.group_send)("teste", {"type": "receive_message", "command": intent.command.script})

        return Response({}, status=status.HTTP_201_CREATED)


class DevicesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer


class CommandsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Commands.objects.all()
    serializer_class = CommandsSerializer


class IntentsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Intents.objects.all()
    serializer_class = IntentsSerializer

@method_decorator(login_required, name='dispatch')
class Dashboard(TemplateView):
    template_name = "dashboard.html"
    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        date_today = datetime.today()
        context["command_by_day"] = ExecutionIntentsLogs.objects.filter(created_at=date_today, intent__device__owner=self.request.user).count()
        context["command_by_month"] = ExecutionIntentsLogs.objects.filter(
            created_at__year=date_today.year, 
            created_at__month=date_today.month,  
            intent__device__owner=self.request.user
        ).count()
        context["qtd_devices"] = Devices.objects.filter(owner=self.request.user).count()
        context["qtd_commands"] = Commands.objects.filter(owner=self.request.user).count()
        return context

class AddDevice(TemplateView):
    template_name = "devices/add.html"

    def post(self, request, *args, **kwargs):
        device_name = request.POST.get("device_name")
        Devices.objects.create(name=device_name, owner=self.request.user)
        return redirect("list_devices")


class ListDevices(TemplateView):
    template_name = "devices/list.html"

    def get_context_data(self, **kwargs):
        context = super(ListDevices, self).get_context_data(**kwargs)
        devices = Devices.objects.filter(owner=self.request.user)
        context["devices"] = devices

        return context


class AddCommand(TemplateView):
    template_name = "commands/add.html"

    def post(self, request, *args, **kwargs):
        command_name = request.POST.get("name")
        plataform = request.POST.get("plataform")
        script = request.POST.get("script")

        Commands.objects.create(name=command_name, plataform=plataform, script=script, owner=self.request.user)
        return redirect("list_commands")


class ListCommands(TemplateView):
    template_name = "commands/list.html"

    def get_context_data(self, **kwargs):
        context = super(ListCommands, self).get_context_data(**kwargs)
        commands = Commands.objects.filter(owner=self.request.user)
        context["commands"] = commands

        return context


class AddIntent(TemplateView):
    template_name = "intents/add.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        device_id = request.POST.get("device")
        command_id = request.POST.get("command")

        device = Devices.objects.get(id=device_id)
        command = Commands.objects.get(id=command_id)

        Intents.objects.create(name=name, device=device, command=command)

        return redirect("intent_list")

    def get_context_data(self, **kwargs):
        context = super(AddIntent, self).get_context_data(**kwargs)
        commands = Commands.objects.all()
        devices = Devices.objects.filter(owner=self.request.user)
        context["commands"] = commands
        context["devices"] = devices

        return context


class ListIntent(TemplateView):
    template_name = "intents/list.html"

    def get_context_data(self, **kwargs):
        context = super(ListIntent, self).get_context_data(**kwargs)
        intents = Intents.objects.filter(device__owner=self.request.user)
        context["intents"] = intents

        return context
