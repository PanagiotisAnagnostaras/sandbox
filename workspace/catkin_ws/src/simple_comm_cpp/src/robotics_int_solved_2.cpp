/*
Ben wrote this node at 4AM... can you spot his mistakes?
*/
#include <sstream>
#include <thread>

#include "ros/ros.h"
#include "std_msgs/Int32MultiArray.h"
#include "std_msgs/String.h"

class DrungPublisher {
 public:
  DrungPublisher(ros::NodeHandle nh) : nh_(nh) {
    chatter_pub_ = nh_.advertise<std_msgs::String>("chatter", 1000);
    array_pub_ = nh_.advertise<std_msgs::Int32MultiArray>("array", 0);
    ros::Timer timer = nh_.createTimer(ros::Duration(1.0),
                                       &DrungPublisher::_timerCallback, this);
    std::thread thread_main_loop(&DrungPublisher::_main_loop, this);
    ros::spin();
  };
  ~DrungPublisher() {};

 private:
  void _timerCallback(const ros::TimerEvent& event) {
    std::vector<int> my_array = std::vector<int>(1000, 0);
    std_msgs::Int32MultiArray msg;
    msg.data = my_array;
    array_pub_.publish(msg);
    ROS_INFO("Published an array of size: %lu", msg.data.size());
  };

  void _main_loop() {
    ros::Rate loop_rate(10);
    int count = 0;
    while (ros::ok()) {
      std_msgs::String msg;
      std::stringstream ss;
      ss << "hello world " << count;
      msg.data = ss.str();
      ROS_INFO("%s", msg.data.c_str());
      chatter_pub_.publish(msg);
      loop_rate.sleep();
      ++count;
    }
  }

  ros::NodeHandle nh_;
  ros::Publisher chatter_pub_;
  ros::Publisher array_pub_;
  ros::Timer timer_;
};

int main(int argc, char** argv) {
  ros::init(argc, argv, "dummy");
  ros::NodeHandle n;
  DrungPublisher drungPublisher(n);
  return 0;
}
