import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Use get_package_share_directory to find the path to the rg_description package
    rg_description_path = get_package_share_directory('rg_description')
    
    # Build the full path to the URDF file
    robot_description_path = os.path.join(rg_description_path, 'urdf', 'roseguardian.urdf')

    return LaunchDescription([
        # Declare the robot_description parameter
        DeclareLaunchArgument('robot_description', default_value=robot_description_path, description="Path to the URDF file"),

        # Node to publish the robot's state (robot_state_publisher)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': LaunchConfiguration('robot_description')}]
        ),

        # Optional: Node to publish joint states (joint_state_publisher)
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen'
        ),

        # Optional: RViz visualization (if you have a configuration file)
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz',
            output='screen',
            arguments=['-d', os.path.join(rg_description_path, 'rviz', 'robot.rviz')]
        ),
    ])
