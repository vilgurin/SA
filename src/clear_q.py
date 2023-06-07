from hazelcast import HazelcastClient

# Create a Hazelcast client
client = HazelcastClient()

# Get the Hazelcast queue
queue = client.get_queue("my_queue")

# Clear the queue
queue.clear()
print("size == ", queue.size())