cmake_minimum_required(VERSION 3.0)
project(MyProject)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Source files
set(SOURCES
    src/main.cpp
    src/lambda_functions.cpp
    src/pointers.cpp
    src/classes.cpp
    src/memory_management.cpp
    src/threads_school.cpp
)

find_package(Threads REQUIRED)


# Add executable
add_executable(main ${SOURCES})
target_include_directories(main PRIVATE include)

target_link_libraries(main PRIVATE Threads::Threads)

