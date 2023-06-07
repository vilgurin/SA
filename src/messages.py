from fastapi import FastAPI
from kafka import KafkaConsumer
import threading
app = FastAPI()
MESSAGES = []

@app.get("/")
def not_implemented():
    return "MESSAGES from message " + str(list(MESSAGES))
