#include "ros/ros.h"
#include "std_msgs/String.h"

// Callback function that will be called when a message is received
void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
    // Log the received message to the console
    ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
    // Initialize the ROS node
    ros::init(argc, argv, "listener");

    // Create a handle for the node
    ros::NodeHandle n;

    // Create a subscriber that subscribes to the "chatter" topic
    ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);

    // Keep the node running to listen for incoming messages
    ros::spin();

    return 0;
}

