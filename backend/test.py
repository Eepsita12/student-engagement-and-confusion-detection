import websockets
import asyncio

async def test():
    uri = "ws://127.0.0.1:8000/ws"
    async with websockets.connect(uri) as websocket:
        for _ in range(5):
            msg = await websocket.recv()
            print(msg)

asyncio.run(test())
