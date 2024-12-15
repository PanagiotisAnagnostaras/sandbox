#!/usr/bin/env python

import rospy
from std_msgs.msg import String


class Listener:
    def __init__(self):
        rospy.init_node("listener", anonymous=True)
        rospy.Subscriber("chatter", String, self.callback)

    def callback(self, data):
        rospy.loginfo("I heard: %s", data.data)

    def listen(self):
        rospy.spin()


if __name__ == "__main__":
    listener = Listener()
    listener.listen()
