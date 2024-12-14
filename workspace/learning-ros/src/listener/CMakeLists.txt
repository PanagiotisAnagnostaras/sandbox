cmake_minimum_required(VERSION 3.0.2)
project(listener)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)
catkin_package()


include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(listener src/listener.cpp)
target_link_libraries(listener ${catkin_LIBRARIES})
