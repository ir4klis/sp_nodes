#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisherA():
	pub = rospy.Publisher('sp_node_a', String, queue_size=3)
	rospy.init_node('publisherA')
	rate = rospy.Rate(1) #update rate in hz
	while not rospy.is_shutdown():
		message_str = "node A"
		rospy.loginfo(message_str)
		pub.publish(message_str)
		rate.sleep()

if __name__ == '__main__':
	try:
		publisherA()
	except rospy.ROSInterruptException:
		pass
