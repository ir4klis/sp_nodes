## ROS sp_nodes package


Package containing two publishers (publisherA.py) and (publisherB.py) and a subscriber (subscriber.py) node.   
Each publisher has its own topic (sp_node_a and sp_node_b) and subscriber subscribes to both of them.  
Quick way to test communication between multiple machines.  

Runs with :  
`$ rosrun sp_nodes <script name>`

Nodes and topics can be seen with   

rosnode list  
`/ab_subscriber`  
`/publisherA`  
`/publisherB`  

rostopic list   
`/sp_node_a`  
`/sp_node_b`  

### If you stumbled upon this and want to know more, [wiki.ros](http://wiki.ros.org)
