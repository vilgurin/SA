from fastapi import FastAPI, HTTPException
import requests
import uuid
from pydantic import BaseModel
import random
from kafka import KafkaProducer


app = FastAPI()

logging_service_url = "http://127.0.0.1:8001/"
LOG_URLS = ["http://127.0.0.1:8001/","http://127.0.0.1:8002/","http://127.0.0.1:8003/"]
MESSAGES_URLS = ["http://127.0.0.1:8004/"]

class Data(BaseModel):
    text: str

class Message(BaseModel):
    msg_id: str
    text: str

def choose_random_url(urls):
    url = random.choice(urls)
    return url

@app.post("/")
def create_message(msg: Data):
    try:
        msg_id = str(uuid.uuid4())
        m = Message(msg_id=msg_id, text=msg.text)
        logging_service_url = choose_random_url(LOG_URLS)
        requests.post(logging_service_url, json=m.dict())
        return {"message_id": msg_id}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Error creating message")

@app.get("/")
def get_messages():
    logging_service_url = choose_random_url(LOG_URLS)
    messages_service_url = choose_random_url(MESSAGES_URLS)
    try:
        response_logging = requests.get(logging_service_url)
        response_logging.raise_for_status()

        response_messages = requests.get(messages_service_url)
        response_messages.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Error retrieving messages")

    response = f"{response_logging.text} {response_messages.text}"
    return response