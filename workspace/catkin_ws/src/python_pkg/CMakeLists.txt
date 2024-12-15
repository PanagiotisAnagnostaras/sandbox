cmake_minimum_required(VERSION 3.0.2)
project(python_pkg)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)
catkin_package()

###########
## Build ##
###########


#############
## Install ##
############
catkin_install_python(PROGRAMS src/talker.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
#############
## Testing ##
#############