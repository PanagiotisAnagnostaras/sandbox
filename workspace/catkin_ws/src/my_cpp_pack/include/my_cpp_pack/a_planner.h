#include "ros/ros.h"
#include <std_msgs/Int16.h>

namespace APlanner {
class APlanner {
 public:
  APlanner(ros::NodeHandle n);
  // void run();

 private:
  int computeSmt();
  void sub_cb(const std_msgs::Int16::ConstPtr &str_msgs);
  void timer_cb(const ros::TimerEvent &event);
  int prev_;
  int x_;
  ros::NodeHandle n_;
  ros::Rate rate_;
  ros::Publisher pub_;
  ros::Subscriber sub_;
  ros::Timer timer_;
};
}  // namespace APlanner