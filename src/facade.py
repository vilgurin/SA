from fastapi import FastAPI
import requests
import uuid
from pydantic import BaseModel
import random
from kafka import KafkaProducer


app = FastAPI()

logging_service_url = "http://127.0.0.1:8001/"
LOG_URLS = ["http://127.0.0.1:8001/","http://127.0.0.1:8002/","http://127.0.0.1:8003/"]
# messages_service_url = "http://127.0.0.1:8004/"
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
    msg_id = str(uuid.uuid4()) 
    m = Message(msg_id=msg_id, text=msg.text)
    logging_service_url = choose_random_url(LOG_URLS)
    requests.post(logging_service_url, json=m.dict())
    # post messages using producer
    post_queue(msg_id, msg.text)


    return 

@app.get("/")
def get_messages():
    logging_service_url = choose_random_url(LOG_URLS)
    response_logging = requests.get(logging_service_url)
    messages_service_url = choose_random_url(MESSAGES_URLS)
    response_messeges = requests.get(messages_service_url)
    response = str(response_logging.text) + " " + str(response_messeges.text)
    return response

def post_queue(id,msg):
    producer = KafkaProducer(bootstrap_servers='localhost:9092', api_version=(0,11,5))
    producer.send('incoming_messages_topic', key = id.encode("utf-8"), value = msg.encode("utf-8"))
    producer.flush()

