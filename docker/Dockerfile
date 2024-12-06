# FROM osrf/ros:humble-desktop-full
FROM nvidia/opengl:base-ubuntu22.04

# 環境変数の設定
ENV ROS_DISTRO humble
ENV ROS_WS ros2_ws

ARG PACKAGE_SUFFIX=cuda12.2
ARG DEBIAN_FRONTEND=noninteractive

ENV __NV_PRIME_RENDER_OFFLOAD=1
ENV __GLX_VENDOR_LIBRARY_NAME=nvidia

# tools
RUN apt-get -qq update && apt-get -q -y install \
    gnupg2 \
    curl \
    ca-certificates \
    build-essential \
    git \
    gh \
    tmux \
    nano \
    wget \
    net-tools \
    blender \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -qq clean

# ROSのリポジトリをsource listに追加
ENV UBUNTU_CODENAME=focal
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null

# ROS2のインストール
RUN apt-get update && apt-get install -y \
    ros-humble-desktop

# colconのインストール
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-argcomplete \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -qq clean

RUN rosdep init && \
    rosdep update

# ipopt
RUN apt-get update && apt-get install -y \
    coinor-libipopt-dev \
    gfortran \
    libblas-dev \
    liblapack-dev \
    libmetis-dev

# ros packages
RUN apt-get update && apt-get install -y \
    ros-${ROS_DISTRO}-pcl-* \
    ros-${ROS_DISTRO}-geometry2 \
    ros-${ROS_DISTRO}-teleop-twist-keyboard \
    ros-${ROS_DISTRO}-navigation2 \
    ros-${ROS_DISTRO}-nav2-bringup \
    ros-${ROS_DISTRO}-joy \
    ros-${ROS_DISTRO}-gazebo-* \
    ros-${ROS_DISTRO}-rqt-* \
    ros-${ROS_DISTRO}-rviz-* \
    ros-${ROS_DISTRO}-xacro \
    ros-${ROS_DISTRO}-robot-localization \
    ros-${ROS_DISTRO}-ros2-controllers \
    ros-${ROS_DISTRO}-ros2-control \
    ros-${ROS_DISTRO}-velodyne \
    ros-${ROS_DISTRO}-velodyne-gazebo-plugins \
    ros-${ROS_DISTRO}-velodyne-description \
    ros-${ROS_DISTRO}-diagnostic-updater \
    ros-${ROS_DISTRO}-nav2-behavior-tree \
    ros-${ROS_DISTRO}-behaviortree-cpp-v3

# other packages
RUN curl -sSL https://eieiof11.github.io/ppa/ppa.key -o /usr/share/keyrings/ppa.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ppa.gpg] https://eieiof11.github.io/ppa $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ppa.list > /dev/null
RUN echo "yaml https://eieiof11.github.io/ppa/rosdep.yaml" | tee /etc/ros/rosdep/sources.list.d/99-ppa.list > /dev/null

RUN curl -s --compressed "https://koide3.github.io/ppa/ubuntu2204/KEY.gpg" | gpg --dearmor | tee /etc/apt/trusted.gpg.d/koide3_ppa.gpg >/dev/null
RUN echo "deb [signed-by=/etc/apt/trusted.gpg.d/koide3_ppa.gpg] https://koide3.github.io/ppa/ubuntu2204 ./" | tee /etc/apt/sources.list.d/koide3_ppa.list
RUN apt-get update
RUN sudo apt install -y libboost-all-dev libglfw3-dev libmetis-dev

RUN apt-get install --no-install-recommends -y \
    libiridescence-dev\
    libgtsam-points-${PACKAGE_SUFFIX}-dev\
    ros-humble-glim-ros-${PACKAGE_SUFFIX}

RUN sudo apt update && rosdep update

RUN apt-get update && apt-get install -y \
    ros-${ROS_DISTRO}-casadi-ament \
    ros-${ROS_DISTRO}-jsk* \
    ros-${ROS_DISTRO}-twist-switcher \
    ros-${ROS_DISTRO}-extension-node \
    ros-${ROS_DISTRO}-data-logger \
    ros-${ROS_DISTRO}-common-utils \
    ros-${ROS_DISTRO}-people-msgs

# make ros2 workspace
RUN mkdir -p /home/user/$ROS_WS/src
WORKDIR /home/user/$ROS_WS
RUN /bin/bash -c "source /opt/ros/$ROS_DISTRO/setup.bash && colcon build --symlink-install"

# install the lightsfm library
RUN git clone https://github.com/robotics-upo/lightsfm.git \
    && cd lightsfm && make && make install

# 環境設定
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc
RUN echo "source /usr/share/gazebo/setup.sh" >> ~/.bashrc
RUN echo "source /home/user/$ROS_WS/install/local_setup.bash" >> ~/.bashrc
RUN echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc
RUN echo "export _colcon_cd_root=/home/user/$ROS_WS" >> ~/.bashrc
