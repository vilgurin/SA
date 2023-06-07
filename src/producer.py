import hazelcast
import threading

client = hazelcast.HazelcastClient()

queue = client.get_queue("my_queue").blocking()

def produce():
    for i in range(100):
        print(f"Producer puts value {i}")
        queue.put(i)

producer_thread = threading.Thread(target=produce)

producer_thread.start()
print("size of queue = ",queue.size())

