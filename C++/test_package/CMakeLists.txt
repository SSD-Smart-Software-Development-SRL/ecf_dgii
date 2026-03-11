cmake_minimum_required(VERSION 3.15)
project(ecf_dgii_client_test CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(ecf-dgii-client REQUIRED)

add_executable(ecf_dgii_client_test src/test.cpp)
target_link_libraries(ecf_dgii_client_test PRIVATE ecf-dgii-client::ecf-dgii-client)
