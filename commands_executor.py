import asyncio
import json
import os
from doctest import OutputChecker

import websockets


async def listen():
    url = "ws://localhost:5000/ws/commands/"

    async with websockets.connect(url) as ws:
        while True:
            msg = await ws.recv()
            message = json.loads(msg)
            print("Executando novo comando", message)
            # os.system(message["command"])
            print("\n")


asyncio.get_event_loop().run_until_complete(listen())
