#include "my_cpp_pack/a_planner.h"


int main(int argc, char** argv) {
  ros::init(argc, argv, "my_node");
  ros::NodeHandle n;
  APlanner::APlanner a_planner(n);
  
  // ros::spin();
  // or
  ros::AsyncSpinner spinner(3);
  spinner.start();

  ros::waitForShutdown();

  return 0;
}