FROM osrf/ros:noetic-desktop-full

RUN apt-get update && apt-get install -y \
    python3-rosdep \
    python3-rosinstall \
    python3-rosinstall-generator \
    python3-wstool \
    build-essential \
    vim \
    nano \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /workspace

RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

CMD ["bash"]
