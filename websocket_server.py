"""
This module implements a WebSocket server for handling emotion data.
"""

import asyncio
import websockets


async def echo(websocket, path):  # pylint: disable=unused-argument
    """
    Receives a message from the client and sends it back as a response.

    Parameters:
    websocket: The WebSocket connection to the client.
    path: The URL path of the WebSocket request (unused in this example).
    """
    async for message in websocket:
        print(f"Received: {message}")
        # Send the received message back to the client
        await websocket.send(f"Echo: {message}")


async def main():
    """
    Starts the WebSocket server on localhost at port 8765.
    The server listens for incoming WebSocket connections and passes
    them to the echo handler.
    """
    async with websockets.serve(echo, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Keep the server running indefinitely


if __name__ == "__main__":
    # Run the WebSocket server
    asyncio.run(main())
