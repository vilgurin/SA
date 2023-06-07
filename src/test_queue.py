import subprocess
from hazelcast import HazelcastClient


subprocess.Popen(['python', 'producer.py'])
subprocess.Popen(['python', 'client.py', "1"])
subprocess.Popen(['python', 'client.py', "2"])