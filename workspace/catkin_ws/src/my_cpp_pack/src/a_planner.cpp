#include "my_cpp_pack/a_planner.h"

namespace APlanner {
APlanner::APlanner(ros::NodeHandle n) : n_(n), rate_(10), prev_(0) {
  pub_ = n_.advertise<std_msgs::Int16>("cpp_topic_out", 10);
  sub_ = n_.subscribe<std_msgs::Int16>("cpp_topic_in", 1, &APlanner::sub_cb, this);
  timer_ = n_.createTimer(ros::Duration(1), &APlanner::timer_cb, this);
  x_ = 0;
};

// void APlanner::run() {
//   while (ros::ok()) {
//     int val = computeSmt();
//     std_msgs::Int16 msg;
//     msg.data = val;
//     pub_.publish(msg);
//     rate_.sleep();
//   }
// }

void APlanner::sub_cb(const std_msgs::Int16::ConstPtr &str_msgs) {
  x_ = str_msgs->data;
  ROS_INFO_STREAM("Subcriber callback = " << x_);
}

void APlanner::timer_cb(const ros::TimerEvent &event) {
  int val = computeSmt();
  std_msgs::Int16 msg;
  msg.data = val;
  pub_.publish(msg);
  ROS_INFO_STREAM("Timer Callback = " << x_);
}

int APlanner::computeSmt() {
  prev_ += 1;
  return prev_;
}
}  // namespace APlanner