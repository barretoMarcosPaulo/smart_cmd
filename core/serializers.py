from rest_framework import serializers

class ReceiveCommandSerializer(serializers.Serializer):
    action = serializers.CharField(max_length=200, required=True)



