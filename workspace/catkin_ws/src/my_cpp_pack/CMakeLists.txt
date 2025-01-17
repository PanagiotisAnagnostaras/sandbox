cmake_minimum_required(VERSION 3.0.2)
project(my_cpp_pack)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)

set(SRC_FILES
  "src/my_node.cpp"
  "src/a_planner.cpp")

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
  include
)

add_executable(my_node ${SRC_FILES})
target_link_libraries(my_node ${catkin_LIBRARIES})
