cmake_minimum_required(VERSION 3.0.2)
project(simple_comm_cpp)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(talker src/talker.cpp)
target_link_libraries(talker ${catkin_LIBRARIES})

add_executable(listener src/listener.cpp)
target_link_libraries(listener ${catkin_LIBRARIES})

add_executable(robotics_int_solved src/robotics_int_solved.cpp)
target_link_libraries(robotics_int_solved ${catkin_LIBRARIES})