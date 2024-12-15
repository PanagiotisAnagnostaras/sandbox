#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    # Initialize the ROS node named 'talker'
    rospy.init_node('talker', anonymous=True)

    # Create a publisher that sends String messages on the 'chatter' topic
    pub = rospy.Publisher('chatter', String, queue_size=10)

    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        msg = "Hello ROS world! %s" % rospy.get_time()
        
        # Publish the message
        pub.publish(msg)
        rospy.loginfo(msg)

        # Sleep to maintain the loop rate
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
