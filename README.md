# Usage
In order to start the application you need to start kafka at first:<br>
bin/zookeeper-server-start.sh config/zookeeper.properties<br>
bin/kafka-server-start.sh config/server.properties<br>
bin/kafka-topics.sh --create --topic message_q --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1<br>
Start 3 hazelcast nodes:<br>
hz-start<br>
Repeat the command three times in three separate terminals<br>
Start all the services.<br>
Messages services read all the messages, that are sent to the queue.<br>
If one wants to make several message applications read different messages, he may<br>
use group id, when starting the Consumer. In this case only one service in group will read the message
