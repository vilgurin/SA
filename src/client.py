import hazelcast
import threading
import sys
index = sys.argv[1]
client = hazelcast.HazelcastClient()

queue = client.get_queue("my_queue")

def consume(index):
    consumed_count = 0
    while True: 
        head = queue.poll().result()
        if head == None:
            continue
        print(f"Client number {index} consuming {head}")
        consumed_count += 1


consumer_thread = threading.Thread(target=consume, args = [index])
consumer_thread.start()