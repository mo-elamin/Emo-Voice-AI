"""
This module implements a WebSocket server for handling emotion data.
"""

import asyncio
import websockets

async def echo(websocket, path):  # pylint: disable=unused-argument
    """
    Receives a message from the client and sends it back as a response.
    """
    async for message in websocket:
        print(f"Received: {message}")
        await websocket.send(f"Echo: {message}")


async def main():
    """
    Starts the WebSocket server on localhost at port 8765.
    """
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
