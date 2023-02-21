# from flask import Flask , jsonify, render_template, request , stream_with_context , Response
from fastapi import FastAPI , Response 
from json import loads  
from kafka import KafkaConsumer
import json
from datetime import datetime
import time
import pandas as pd
import numpy as np
 
import asyncio
from fastapi import Request
from fastapi import WebSocket
from fastapi.templating import Jinja2Templates


my_consumer = KafkaConsumer(  
    'testnum',  
    bootstrap_servers = ['localhost : 9092'],  
    auto_offset_reset = 'earliest',  
    enable_auto_commit = True,  
    group_id = 'my-group',  
    value_deserializer = lambda x : loads(x.decode('utf-8'))  
    )

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:

        my_consumer = KafkaConsumer(  
        'testnum',  
        bootstrap_servers = ['localhost : 9092'],  
        auto_offset_reset = 'earliest',  
        enable_auto_commit = True,  
        group_id = 'my-group',  
        value_deserializer = lambda x : loads(x.decode('utf-8'))  
        )
        for message in my_consumer:
            measurements = message.value
            await asyncio.sleep(1)
            # json_data = json.dumps(
            #     {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': measurements})

            try:
                await websocket.send_json(measurements)
            except:
                print("Close")

