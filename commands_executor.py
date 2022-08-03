import asyncio
import json
import os

import websockets


async def listen():
    url = "ws://localhost:8000/ws/commands/"

    async with websockets.connect(url) as ws:
        while True:
            msg = await ws.recv()
            message = json.loads(msg)
            # cmd = message["data"]["command"]
            print(">_ ", message)
            # os.system(cmd)


asyncio.get_event_loop().run_until_complete(listen())
