import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Get the share directory of the 'rg_description' package
    pkg_share = get_package_share_directory('rg_description')

    # Specify the path to the URDF file
    urdf_file = os.path.join(pkg_share, 'urdf', 'roseguardian.URDF')

    # Define the launch description
    return LaunchDescription([

        # Declare URDF file argument (optional for flexibility)
        DeclareLaunchArgument(
            'urdf_file',
            default_value=urdf_file,
            description='Path to the robot URDF file'
        ),

        # Load the URDF file into the parameter server directly (no xacro processing needed)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': LaunchConfiguration('urdf_file')}]
        ),

        # Launch Rviz with the robot model
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(pkg_share, 'rviz', 'default.rviz')]
        )
    ])
