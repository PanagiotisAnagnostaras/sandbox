#!/usr/bin/env python

import rospy
from std_msgs.msg import String

class Listener:
    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber('chatter', String, callback)
        
    def callback(data):
        rospy.loginfo("I heard: %s", data.data)

    def listen():
        rospy.spin()

if __name__ == '__main__':
    listener = Listener()
    listener.listen()
