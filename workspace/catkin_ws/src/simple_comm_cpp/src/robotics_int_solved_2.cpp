/*
Ben wrote this node at 4AM... can you spot his mistakes?
*/
#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Int32MultiArray.h"

#include <sstream>

void timerCallback(const ros::TimerEvent&) {
        std::vector<int> my_array = new std::vector<int>(1000, 0);
        std_msgs::Int32MultiArray msg;
        msg.data = *my_array;
        pub_.publish(msg);
        ROS_INFO("Published an array of size: %lu", msg.data.size());
    }

int main(int argc, char **argv)
{
  ros::init(argc, argv, "dummy");
  ros::NodeHandle n;
  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);
  ros::Publisher array_pub = n.advertise<std_msgs::UInt8MultiArray>("array", 0);
  ros::Timer timer = nh.createTimer(ros::Duration(1.0), timerCallback, n);

  ros::Rate loop_rate(10);

  int count = 0;
  while (ros::ok())
  {
    std_msgs::String* msg;

    std::stringstream ss;
    ss << "hello world " << count;
    msg.data = ss.str();

    ROS_INFO("%s", msg.data.c_str());
    chatter_pub.publish(msg);

    loop_rate.sleep();
    ++count;
  }


  return 0;
}

