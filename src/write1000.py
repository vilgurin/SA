from hazelcast import HazelcastClient
def put_1000(map):
    for i in range(1000):
        map.put(i, i)

def show(map, key):
    value = map.get(key)
    print(f"Key: {key}, Value: {value}")

client = HazelcastClient()
my_map = client.get_map("my-distributed-map").blocking()
put_1000(my_map)
show(my_map, 10)
client.shutdown()
