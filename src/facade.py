from fastapi import FastAPI, HTTPException
import requests
import uuid
from pydantic import BaseModel
import random
from kafka import KafkaProducer

app = FastAPI()

logging_service_url = "http://127.0.0.1:8001/"
LOG_URLS = ["http://127.0.0.1:8001/","http://127.0.0.1:8002/","http://127.0.0.1:8003/"]
MESSAGES_URLS = [
    "http://localhost:8004/",
    "http://localhost:8005/",
]

class Data(BaseModel):
    text: str

class Message(BaseModel):
    msg_id: str
    text: str

def choose_random_url(urls):
    url = random.choice(urls)
    return url

@app.post("/")
async def create_message(msg: Data):
    try:
        msg_id = str(uuid.uuid4())
        m = Message(msg_id=msg_id, text=msg.text)
        logging_service_url = choose_random_url(LOG_URLS)
        requests.post(logging_service_url, json=m.dict())
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Error creating message")
    try:
        post_queue(msg_id, msg.text)
    except:
        raise HTTPException(status_code=500, detail="Error posting to queue")
    return {"message_id": msg_id}

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

def post_queue(id,msg):
    try:
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
    except:
        raise HTTPException(status_code=500, detail="Error creating producer")
    try:
        producer.send('message_q', key = id.encode("utf-8"), value = msg.encode("utf-8"))
    except:
        raise HTTPException(status_code=500, detail="Error sending messages to queue")
    producer.flush()

