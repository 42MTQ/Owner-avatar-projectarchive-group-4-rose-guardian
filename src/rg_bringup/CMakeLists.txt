cmake_minimum_required(VERSION 3.8)
project(rg_bringup)

# Specify additional compiler flags (optional)
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rviz2 REQUIRED)
find_package(rclcpp REQUIRED)
find_package(urdf REQUIRED)
find_package(robot_state_publisher REQUIRED)  # Needed for publishing URDF in RViz

# Uncomment the following section if you have more dependencies
# find_package(<dependency> REQUIRED)

# Add your launch file directory to CMake install process

# Handle testing and linting if enabled
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)


# Declare the package
ament_package()
