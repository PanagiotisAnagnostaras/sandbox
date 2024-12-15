# Nodes
rosnode list
rosrun PKG NODE

# Topics
rostopic ...

# Packages
rospack list
rospack find PKG_NAME

# How to setup the workspace

## Catkin workspace

```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_init_workspace
catkin_make
```

## Packages
### C++ Packages
```
catkin_create_pkg PKG_NAME std_msgs roscpp
```
place source code under `pkg_name/src` and modify `CMakeLists.txt` and `package.xml`

Build and source workspace
```
catkin_make
source devel/setup.bash
```
Start ros
```
roscore
```
Run nodes
```
rosrun PKG NODE_NAME
```
### Python Packages
```
catkin_create_pkg PKG_NAME rospy std_msgs
```