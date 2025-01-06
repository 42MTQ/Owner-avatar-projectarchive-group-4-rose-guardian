import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    
    rg_description_path = get_package_share_directory('rg_description')
    
    
    robot_description_path = os.path.join(rg_description_path, 'URDF', 'roseguardian.URDF')

    return LaunchDescription([
       
        DeclareLaunchArgument('robot_description', default_value=robot_description_path, description="Path to the URDF file"),

       
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': LaunchConfiguration('robot_description')}]
        ),

        
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen'
        ),

        
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz',
            output='screen',
            arguments=['-d', os.path.join(rg_description_path, 'rviz', 'robot.rviz')]
        ),
    ])
