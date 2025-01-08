import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Get package paths
    roseguardian_gazebo_share_path = get_package_share_directory('roseguardian_gazebo')
    roseguardian_control_share_path = get_package_share_directory('roseguardian_control')
    
    world_file_path = os.path.join(roseguardian_gazebo_share_path, 'worlds', 'farmWith1CropRow.world')
    urdf_file_path = os.path.join(roseguardian_control_share_path, 'urdf', 'roseguardian.xacro')

    return LaunchDescription([
        
        # Declare launch arguments
        DeclareLaunchArgument('paused', default_value='false', description='Pause the simulation at start'),
        DeclareLaunchArgument('use_sim_time', default_value='true', description='Use simulation time'),
        DeclareLaunchArgument('gui', default_value='true', description='Launch GUI'),
        DeclareLaunchArgument('headless', default_value='false', description='Run Gazebo in headless mode'),
        DeclareLaunchArgument('debug', default_value='false', description='Enable debugging'),
        DeclareLaunchArgument('real_time_update_rate', default_value='true', description='Enable real-time update rate'),

        # Launch Gazebo with the specified world file
        Node(
            package='gazebo_ros',
            executable='gzserver',
            name='gazebo',
            output='screen',
            arguments=['-s', world_file_path]
        ),

        # Spawn the robot in Gazebo from the URDF file
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_robot',
            output='screen',
            arguments=[
                '-entity', 'roseguardian',  # Robot name in Gazebo
                '-file', urdf_file_path,  # Path to URDF/Xacro
                '-x', '0', '-y', '0', '-z', '1.0', '-Y', '0'  # Spawn position and orientation
            ]
        ),
    ])
