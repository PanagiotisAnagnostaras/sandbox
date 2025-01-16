import rospy
from std_msgs.msg import Int16


class StateEstimator:
    def __init__(self) -> None:
        self._pub = rospy.Publisher("cpp_topic_in", Int16, queue_size=1)
        self._sub = rospy.Subscriber("cpp_topic_out", Int16, self._sub_cb)
        self._timer = rospy.Timer(rospy.Duration(1.0), callback=self._timer_cb)
        self.x = 0
        self.y = 0
        self.theta = 0
    
    def _sub_cb(self, msg: Int16):
        rospy.loginfo(f"StateEstimator got = {msg.data}")
        
    def _timer_cb(self, event):
        self._do_smt()
        self._pub.publish(self.x)
        rospy.loginfo("I did something")
        
    def _do_smt(self):
        self.x += 1
        self.y += 1
        self.theta += 1
