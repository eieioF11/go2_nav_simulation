# go2_nav_simulation
Simulation environment for go2 navigation tests

https://youtu.be/Hd2WPup5Wb0
![image](https://github.com/user-attachments/assets/7eef7d8e-78dd-4015-bb22-ccbb6c575f28)

# Installation
## Install lightsfm
https://github.com/robotics-upo/lightsfm?tab=readme-ov-file
```bash
git clone https://github.com/robotics-upo/lightsfm.git
cd lightsfm
make
sudo make install
```

## Dependency Installation
```bash
sudo apt install ros-$ROS_DISTRO-gazebo-ros2-control
sudo apt install ros-$ROS_DISTRO-xacro
sudo apt install ros-$ROS_DISTRO-robot-localization
sudo apt install ros-$ROS_DISTRO-ros2-controllers
sudo apt install ros-$ROS_DISTRO-ros2-control
sudo apt install ros-$ROS_DISTRO-velodyne
sudo apt install ros-$ROS_DISTRO-velodyne-gazebo-plugins
sudo apt-get install ros-$ROS_DISTRO-velodyne-description
```

## Clone repository
```bash
cd ros2_ws/src
git clone --recursive https://github.com/eieioF11/go2_nav_simulation.git
rosdep update
rosdep install -yi --rosdistro humble --from-paths .
cd ../
colcon build --symlink-install
```
