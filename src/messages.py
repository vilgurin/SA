from fastapi import FastAPI
from kafka import KafkaConsumer
import threading
app = FastAPI()
MESSAGES = []

@app.get("/")
def not_implemented():
    return "MESSAGES from message " + str(list(MESSAGES))

def read_from_queue():
    try:
        consumer = KafkaConsumer('incoming_messages_topic', bootstrap_servers='localhost:9092',auto_offset_reset='earliest', api_version=(0,11,5))
        for message in consumer:
            MESSAGES.append(message.value.decode('utf-8'))
            print("messages accepted")
    except Exception as e:
        print(f"An error occurred while consuming messages: {str(e)}")

t = threading.Thread(target=read_from_queue)
t.start()