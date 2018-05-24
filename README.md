## ROS sp_nodes package


Package containing two publisherers (publisherA.py) and (publisherB.py) and a subscriber (subscriber.py) nodes.   
Each publisher publishes to its own node (sp_node_a and sp_node_b) and subscriber subscribes to both of them.  
Quick way to test communication between multiple machines.  

Runs with :  
`$ rosrun <pkg name> <script name>`

Nodes and topics can be seen with   

rosnode list  
`/ab_subscriber`  
`/publisherA`  
`/publisherB`  
/rosout

rostopic list  
/rosout  
/rosout_agg  
`/sp_node_a`  
`/sp_node_b`  

### If you stumbled upon this and want to know more, [wiki.ros](http://wiki.ros.org)
