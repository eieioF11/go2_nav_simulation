#!/bin/bash
set -e
g_setup=/opt/ros/humble/setup.bash
l_setup=/root/ros2_ws/install/local_setup.bash
if [ -e $g_setup ]; then
   source $g_setup
else
   echo "$g_setup not found"
fi
if [ -e $l_setup ]; then
   source $l_setup
else
   echo "$l_setup not found"
fi
exec "$@"