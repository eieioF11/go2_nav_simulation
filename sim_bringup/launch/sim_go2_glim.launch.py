import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
import launch


def generate_launch_description():
    pkg_dir = get_package_share_directory('sim_bringup')
    launch_list = [
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            arguments=[
                "--x",
                "0.0",
                "--y",
                "0.0",
                "--z",
                "0.0",
                "--yaw",
                "0.0",
                "--pitch",
                "0.0",
                "--roll",
                "0.0",
                "--frame-id",
                "imu",
                "--child-frame-id",
                "livox",
            ],
        ),
        Node(
            package="glim_ros",
            executable="glim_rosnode",
            output="screen",
            parameters=[
                {"config_path": os.path.join(pkg_dir, "config", "sim_go2_glim")},
                {"debug" : False}
            ]
        ),
    ]

    return LaunchDescription(launch_list)
