#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "  Recieving: %s", data.data)
    
def subscriber():


    rospy.init_node('ab_subscriber')

    rospy.Subscriber("sp_node_a", String, callback)
    rospy.Subscriber("sp_node_b", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    subscriber()
