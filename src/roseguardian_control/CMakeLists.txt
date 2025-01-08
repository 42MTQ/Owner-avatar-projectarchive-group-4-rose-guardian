cmake_minimum_required(VERSION 3.5)
project(roseguardian_control)

# Ensure ament is used instead of catkin
find_package(ament_cmake REQUIRED)

# ROS 2 package dependencies
find_package(rclcpp REQUIRED)
find_package(urdf REQUIRED)
find_package(robot_state_publisher REQUIRED)


# Declare your package and its dependencies
ament_package()

# Install the directories (config, launch, meshes, urdf)


install(  
  DIRECTORY config  
  DESTINATION share/${PROJECT\_NAME}  
)  
install(  
  DIRECTORY launch  
  DESTINATION share/${PROJECT\_NAME}  
)  

install(  
  DIRECTORY meshes  
  DESTINATION share/${PROJECT\_NAME}  
)  


install(  
  DIRECTORY urdf  
  DESTINATION share/${PROJECT\_NAME}  
)  


