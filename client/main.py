import asyncio
import websockets


async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world from client")
        server_msg = await websocket.recv()
        print(f"reseived: {server_msg}")

asyncio.get_event_loop().run_until_complete(hello('ws://localhost:8080'))
