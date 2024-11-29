import os
import sys
from glob import glob
from launch_ros.descriptions import ComposableNode
from launch_ros.actions import Node
from launch_ros.actions import ComposableNodeContainer
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    pkg_dir = get_package_share_directory("sim_bringup")
    list = [
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [os.path.join(pkg_dir, "launch"), "/go2_hunav_sim.launch.py"]
            ),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [os.path.join(pkg_dir, "launch"), "/sim_go2_glim.launch.py"]
            ),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [os.path.join(pkg_dir, "launch"), "/sim_go2_glim.launch.py"]
            ),
        ),
        Node(
            package='joy',
            executable='joy_node',
            namespace='',
            output="screen",
            respawn=True,
        ),
        Node(
            package='twist_switcher',
            executable='twist_switcher',
            namespace='',
            output="screen",
            parameters=[os.path.join(pkg_dir, "config", "twist_switcher_param.yaml")],
            respawn=True,
        ),
    ]

    return LaunchDescription(list)
