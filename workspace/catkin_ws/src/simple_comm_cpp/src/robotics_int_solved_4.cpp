/*
Ben wrote this node at 4AM... can you spot his mistakes?
*/
#include <sstream>

#include "ros/ros.h"
#include "std_msgs/Int32MultiArray.h"
#include "std_msgs/String.h"

class Something {
 public:
  Something(ros::NodeHandle n) : n_(n), loop_rate_(10) {
    chatter_pub_ = n_.advertise<std_msgs::String>("chatter", 1000);
    array_pub_ = n_.advertise<std_msgs::Int32MultiArray>("array", 0);
    timer_ =
        n_.createTimer(ros::Duration(1.0), &Something::timerCallback_, this);
  };

  void run() {
    int count = 0;
    while (ros::ok()) {
      std_msgs::String msg;

      std::stringstream ss;
      ss << "hello world " << count;
      msg.data = ss.str();

      ROS_INFO("%s", msg.data.c_str());
      chatter_pub_.publish(msg);

      loop_rate_.sleep();
      ++count;
    }
  }

 private:
  void timerCallback_(const ros::TimerEvent&) {
    std::vector<int> my_array = std::vector<int>(1000, 0);
    std_msgs::Int32MultiArray msg;
    msg.data = my_array;
    array_pub_.publish(msg);
    ROS_INFO("Published an array of size: %lu", msg.data.size());
  }

  ros::NodeHandle n_;
  ros::Publisher chatter_pub_;
  ros::Publisher array_pub_;
  ros::Timer timer_;
  ros::Rate loop_rate_;
};

int main(int argc, char** argv) {
  ros::init(argc, argv, "dummy");
  ros::NodeHandle n;
  Something something = Something(n);
  something.run();
  return 0;
}
