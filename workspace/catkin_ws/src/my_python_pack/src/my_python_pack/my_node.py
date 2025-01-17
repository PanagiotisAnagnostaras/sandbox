import rospy
from my_python_pack.a_state_estimator import StateEstimator

if __name__ == '__main__':
    rospy.init_node('my_python_node')
    state_estimator = StateEstimator()
    rospy.spin()