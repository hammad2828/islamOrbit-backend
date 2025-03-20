import asyncio
import websockets
import json
from utils.func import open_api_call

async def handle_voice_call(websocket, path):
    try:
        print("New client connected")
        while True:
            # Receive message from client
            message = await websocket.recv()
            data = json.loads(message)
            
            # Process the message with GPT
            response = open_api_call(data["text"])
            
            # Send response back to client
            await websocket.send(json.dumps({
                "type": "response",
                "text": response
            }))
            
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {e}")

async def main():
    server = await websockets.serve(
        handle_voice_call,
        "localhost",
        8765
    )
    print("WebSocket server started on ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main()) 