from fastapi import FastAPI
from typing import Dict
from pydantic import BaseModel


app = FastAPI()

messages = {}

class Message(BaseModel):
    msg_id: str
    text: str 

@app.post("/")
def log_message(message: Message):
    messages[message.msg_id] = message.text
    return 


@app.get("/")
def get_messages():
    print(list(messages.values()))
    return str(list(messages.values()))
