# How to setup the workspace

## Catkin workspace

```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```

## Packages
```
catkin_create_pkg listener std_msgs roscpp
catkin_create_pkg talker std_msgs roscpp
```
place source code under `pkg_name/src` and modify `CMakeLists.txt` and `package.xml`

Build and source workspace
```
catkin_make
source devel/setup.bash
```


## Useful commands
```
rostopic info/list
rosrun pkg_name node_name
```