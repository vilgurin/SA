# distributed map with locks 
from hazelcast import HazelcastClient
import time
import threading
client = HazelcastClient()


def no(client):
    my_map = client.get_map("lock").blocking()
    key = 1
    my_map.put(key, 0)

    print("Starting")
    for k in range(1000):
        if k % 100 == 0:
            print("At:", k)
        value = my_map.get(key)
        time.sleep(0.01)
        value  += 1
        my_map.put(key, value)
    
    print("Finished! Result =", my_map.get(key))

def pess(client):
    my_map = client.get_map("lock").blocking()
    key = 1
    my_map.put(key, 0)

    print("Starting")
    for k in range(1000):
        my_map.lock(key)
        try:
            value = my_map.get(key)
            value += 1
            time.sleep(0.01)
            my_map.put(key, value)
        finally:
            my_map.unlock(key)

    print("Finished! Result =", my_map.get(key))

import time
import threading
from hazelcast import HazelcastClient

def optim(client):
    my_map = client.get_map("lock").blocking()
    key = 1
    my_map.put(key, 0)

    print("Starting")
    for k in range(1000):
        if k % 10 == 0:
            print("At:", k)
        while True:
            value = my_map.get(key)
            new_value = value + 1
            time.sleep(0.01)
            if my_map.replace_if_same(key, value, new_value):
                break

    result = my_map.get(key)
    print("Finished! Result =", result)

for i in range(3):
    client = HazelcastClient()
    thread = threading.Thread(target=optim, args=[client])
    thread.start()
