cmake_minimum_required(VERSION 3.8)
project(rg_description)

# Add additional compiler options for GCC or Clang
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rviz2 REQUIRED)
find_package(rclcpp REQUIRED)
find_package(urdf REQUIRED)

# Uncomment the following section to add further dependencies manually:
# find_package(<dependency> REQUIRED)

# Handle testing and linting if enabled
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # Skip linter checks for copyrights if not ready
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# Add package-specific installation commands here if needed

# Declare the package to be managed by ament
ament_package()