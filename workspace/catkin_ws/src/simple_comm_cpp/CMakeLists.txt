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

add_executable(robotics_int_solved_1 src/robotics_int_solved_1.cpp)
target_link_libraries(robotics_int_solved_1 ${catkin_LIBRARIES})

add_executable(robotics_int_solved_2 src/robotics_int_solved_2.cpp)
target_link_libraries(robotics_int_solved_2 ${catkin_LIBRARIES})

add_executable(robotics_int_solved_3 src/robotics_int_solved_3.cpp)
target_link_libraries(robotics_int_solved_3 ${catkin_LIBRARIES})