import os
import sys
from glob import glob
import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
from launch.substitutions import LaunchConfiguration, PythonExpression

def generate_launch_description():
    share_dir = get_package_share_directory('sim_bringup')
    rviz_config_file = os.path.join(share_dir, 'rviz','sim_go2.rviz')
    rviz2_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', rviz_config_file],
    )
    return launch.LaunchDescription(
        [rviz2_node]
    )