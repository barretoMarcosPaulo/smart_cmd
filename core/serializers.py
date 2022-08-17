from rest_framework import serializers

from .models import Commands, Devices, Intents


class ReceiveCommandSerializer(serializers.Serializer):
    action = serializers.CharField(max_length=200, required=True)


class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = "__all__"


class CommandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commands
        fields = "__all__"


class IntentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intents
        fields = "__all__"
