# Use an official Ubuntu base image
FROM ubuntu:20.04

# Set environment variables to make the installation process non-interactive
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies for ROS Noetic and setup repository
RUN apt-get update && apt-get install -y \
    lsb-release \
    gnupg2 \
    curl \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Add the ROS repository
RUN curl -sSL http://packages.ros.org/ros2/ubuntu/ros.asc | sudo tee /etc/apt/trusted.gpg.d/ros.asc
RUN echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/ros-latest.list

# Install ROS Noetic packages
RUN apt-get update && apt-get install -y \
    ros-noetic-desktop-full \
    && rm -rf /var/lib/apt/lists/*

# Set up the environment for ROS Noetic
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

# Install additional dependencies
RUN apt-get update && apt-get install -y \
    python-rosdep \
    python-rosinstall \
    python-rosinstall-generator \
    python-wstool \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Initialize rosdep
RUN rosdep init
RUN rosdep update

# Set working directory
WORKDIR /workspace

# Default command when running the container
CMD ["bash"]
