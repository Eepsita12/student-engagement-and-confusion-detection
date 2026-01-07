from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
from collections import deque

from ai_engine.state_provider import get_current_state

app = FastAPI()

timeline=deque(maxlen=30)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Websocket connected")

    try: 
        while True:
            state=get_current_state()
            timeline.append(state)
            
            payload = {
                "current":state,
                "timeline":list(timeline)
            }

            print("Sending payload:", payload)

            await websocket.send_json(payload)
            await asyncio.sleep(0.5)

    except WebSocketDisconnect:
        print("Websocket disconnected")
    except Exception as e:
        print("Websocket Error: ",e)