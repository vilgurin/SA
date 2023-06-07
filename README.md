3. Start 3 hazelcast nodes in the terminal<br>
Use hz-start<br>
Use the file write100.py to write 1000 values in the map.<br>
Start managment center<br>
In order to do this navigate to the folder with the center, then to bin and use<br>
./start.sh to start the center. Open the location in the internet.<br>
If we use 3 nodes the information will be splited equally (0.33 for each).<br> After we turn off one node,
the distribution will change to approximately 50/50. <br>
4. To check the performance of the distributed map with locks, use map_locks.py with the corresponding parameters.<br>
The program will run 3 instances of each method in threads.<br>
5. In order to create Bounded queue the .xml file needs to modified. Set the max-size to the<br>
desired capacity.If the queue is full, the producer should stop putting values in the queue.<br>
Multiple readers read different values.
