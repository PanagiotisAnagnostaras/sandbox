# Use the official ROS Noetic desktop-full image as the base
FROM osrf/ros:noetic-desktop-full

# Set environment variables to make the installation process non-interactive
ENV DEBIAN_FRONTEND=noninteractive

# Install additional dependencies or tools (if needed)
RUN apt-get update && apt-get install -y \
    python3-rosdep \
    python3-rosinstall \
    python3-rosinstall-generator \
    python3-wstool \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


# Set up the ROS workspace directory (optional)
WORKDIR /workspace

# Set up the environment for ROS Noetic (if not already set in the base image)
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

# Default command when running the container
CMD ["bash"]
