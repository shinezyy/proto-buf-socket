cmake_minimum_required(VERSION 3.5)
project(SocketProtobuf)

find_package(Threads REQUIRED)

include(FindProtobuf)
find_package(Protobuf REQUIRED)

include_directories(${PROTOBUF_INCLUDE_DIR})
include_directories(${CMAKE_BINARY_DIR})
include_directories(SYSTEM)

add_custom_command(
    OUTPUT
    ${CMAKE_BINARY_DIR}/msg.pb.cc
    ${CMAKE_BINARY_DIR}/msg.pb.h
    DEPENDS
    ${PROJECT_SOURCE_DIR}/msg.proto
    COMMAND
        protoc -I=${PROJECT_SOURCE_DIR} --cpp_out=${CMAKE_BINARY_DIR}
            ${PROJECT_SOURCE_DIR}/msg.proto
    VERBATIM
    )

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")
set(CLIENT_SOURCE_FILES client.cpp ${CMAKE_BINARY_DIR}/msg.pb.cc)
set(SERVER_SOURCE_FILES server.cpp ${CMAKE_BINARY_DIR}/msg.pb.cc)
add_executable(client ${CLIENT_SOURCE_FILES})
add_executable(server ${SERVER_SOURCE_FILES})
TARGET_LINK_LIBRARIES( client LINK_PUBLIC ${CMAKE_THREAD_LIBS_INIT}
    ${PROTOBUF_LIBRARY})
TARGET_LINK_LIBRARIES( server LINK_PUBLIC ${CMAKE_THREAD_LIBS_INIT}
    ${PROTOBUF_LIBRARY})
