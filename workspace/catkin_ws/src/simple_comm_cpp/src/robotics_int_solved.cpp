/*
Ben wrote this node at 4AM... can you spot his mistakes?
*/
#include <sstream>
// todo extra paths for autocomplete
#include "ros/ros.h"
#include "std_msgs/Int32MultiArray.h"
#include "std_msgs/String.h"

class Publisher {
 public:
  Publisher(ros::NodeHandle n) : n_(n) {
    chatter_pub_ = n_.advertise<std_msgs::String>("chatter", 1000);
    array_pub_ = n_.advertise<std_msgs::Int32MultiArray>("array", 0);

    ros::Rate loop_rate(10);

    int count = 0;
    timer_ = n_.createTimer(ros::Duration(1), &Publisher::_timerCallback, this);
    while (ros::ok()) {
      ros::spinOnce();
      std_msgs::String msg;

      std::stringstream ss;
      ss << "- world " << count;
      msg.data = ss.str();

      ROS_INFO("%s", msg.data.c_str());
      chatter_pub_.publish(msg);
      loop_rate.sleep();
      ++count;
    }
  };
  ~Publisher() {};

 private:
  void _timerCallback(const ros::TimerEvent& event) {
    std::vector<int> my_array(1000, 0);
    std_msgs::Int32MultiArray msg;
    msg.data = my_array;
    array_pub_.publish(msg);
    ROS_INFO("Published an array of size: %lu", msg.data.size());
  }

  ros::Publisher chatter_pub_;
  ros::Publisher array_pub_;
  ros::Timer timer_;
  ros::NodeHandle n_;
};

int main(int argc, char **argv){
  ros::init(argc, argv, "dummy");
  ros::NodeHandle n;
  Publisher publisher(n);
  return 0;
}