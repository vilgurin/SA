from fastapi import FastAPI
from typing import Dict
from pydantic import BaseModel
import hazelcast

app = FastAPI()
hz = hazelcast.HazelcastClient()
my_map = hz.get_map("my-map").blocking()
messages = {}

class Message(BaseModel):
    msg_id: str
    text: str 

@app.post("/")
def log_message(message: Message):
    add_msg_hz(my_map, message.msg_id, message.text)
    return 

@app.get("/")
def get_messages():
    data = retrieve_data_hz(my_map)
    print(data)
    return data

def add_msg_hz(map,msg_id, msg_text):
    map.put(msg_id,msg_text)

def retrieve_data_hz(map):
    data = map.values()
    return str(list(data))
