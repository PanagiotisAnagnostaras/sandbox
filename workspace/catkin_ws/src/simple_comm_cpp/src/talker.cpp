#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char **argv)
{
    // Initialize the ROS node
    ros::init(argc, argv, "talker");

    // Create a handle for the node
    ros::NodeHandle n;

    // Create a publisher that will publish to the topic "chatter"
    ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);

    // Set the loop rate (10 Hz)
    ros::Rate loop_rate(10);

    // Loop while the ROS node is running
    while (ros::ok())
    {
        // Create the message to be published
        std_msgs::String msg;
        std::stringstream ss;
        ss << "Hello, ROS! " << ros::Time::now();
        msg.data = ss.str();

        // Log the message to the console
        ROS_INFO("%s", msg.data.c_str());

        // Publish the message
        chatter_pub.publish(msg);

        // Sleep to maintain the loop rate
        loop_rate.sleep();
    }

    return 0;
}

