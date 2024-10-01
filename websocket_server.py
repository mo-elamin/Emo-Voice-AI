import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send(f"Message received: {message}")

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # Run forever

asyncio.run(main())
