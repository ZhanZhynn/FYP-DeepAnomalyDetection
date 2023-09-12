import http.client
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sockets import sio_app
import socketio
import asyncio
import json
import requests
import time

app = FastAPI()
# sio = socketio.AsyncServer(cors_allowed_origins="*")
# app.mount("/", socketio.ASGIApp(sio))

sio_server = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

sio_app = socketio.ASGIApp(sio_server)

GENERATE = [False]
CONNECTED = [False]
CONNECTION_BROKE = [False]


# app.mount('/', app=sio_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/ws', sio_app)


@app.get('/')
async def home():
    print('hello')
    return {'message': 'Hello👋 Developers💻'}


# sio_server = socketio.AsyncServer(
#     async_mode='asgi',
#     cors_allowed_origins=[]
# )

# sio_app = socketio.ASGIApp(
#     socketio_server=sio_server,
#     # socketio_path='sockets'
# )


# @sio_server.event
# async def chat(sid, message):
#     print("hello")
#     # await sio_server.emit('chat', {'sid': sid})


# @sio_server.event
# async def connect(sid, environ, auth):
#     print("connect", sid)
#     await sio_server.emit("message", f"connected {sid}", room=sid)


# @sio_server.event
# def disconnect(sid):
#     print("disconnect", sid)

# @sio_server.on('chat')
# async def connected(sid, message):
#     CONNECTED[0] = True
#     if CONNECTION_BROKE[0]:
#         CONNECTION_BROKE[0] = False
#         await chat1("asd", "SAD")


# @sio_server.on('chat2')
# async def chat1(sid, message):
#     print("chat2")
#     GENERATE[0] = True
#     while GENERATE[0]:
#         time.sleep(5)
#         await generate(sid, message)


@sio_server.on('chat2')
async def generate(sid, message):
    counter = 0
    # GENERATE[0] = True

    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

    headers = {
        "accept": "application/json",
        "X-RapidAPI-Key": "insert your key here",
        "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }

    response1 = requests.get(url, headers=headers)
    response1 = response1.json()
    # print(response1)

    dataMessage = response1["value"]

    await sio_server.emit('chat1response', {'message': dataMessage})
    # print(counter)
    print(dataMessage)

    # while GENERATE[0]:
    #     url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

    #     headers = {
    #         "accept": "application/json",
    #         "X-RapidAPI-Key": "e6a6426747msh63d83134cb238fbp1c9435jsnb027b66c84b0",
    #         "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    #     }

    #     response1 = requests.get(url, headers=headers)
    #     response1 = response1.json()
    #     # print(response1)

    #     dataMessage = response1["value"]

    #     await sio_server.emit('chat1response', {'message': dataMessage})
    #     # print(counter)
    #     print(dataMessage)

    #     time.sleep(5)

    # print(response1.json())


@sio_server.on('stopGenerate')
async def stopGenerate(sid, message):
    print("stopGenerate")
    # GENERATE[0] = False


# @sio_server.on('disconnect')
# def stopGenerate1(sid):
#     print("stopGenerate")
    # CONNECTION_BROKE[0] = True
    # GENERATE[0] = False
    # CONNECTED[0] = False

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=5049)

# env/scripts/activate
# uvicorn main:app  --reload  --port 8000
# uvicorn main:app --reload
