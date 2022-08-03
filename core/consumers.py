import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("teste", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("teste", self.channel_name)

    # Receive message from web socket
    async def receive(self, text_data):
        await self.channel_layer.group_send(
            "teste",
            {"type": "receive_message", "command": "teste"},
        )

    async def receive_message(self, event):
        data = event.copy()
        del data["type"]
        await self.send(
            text_data=json.dumps(
                data,
            )
        )

    @sync_to_async
    def save_message(self, useruuid, roomuuid, message):
        pass
