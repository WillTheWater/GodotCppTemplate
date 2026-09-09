cmake_minimum_required(VERSION 3.13)

# Cloning without --recurse-submodules otherwise fails deep inside CMake.
if(NOT EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/godot-cpp/CMakeLists.txt")
    message(FATAL_ERROR "godot-cpp is empty. Run: git submodule update --init --recursive")
endif()

project(godot_cpp_template LANGUAGES CXX)

# Must precede add_subdirectory; cached on first configure.
set(GODOTCPP_API_VERSION "4.7" CACHE STRING "Godot API version to build against")

add_subdirectory(godot-cpp)

add_subdirectory(src/game)

add_library(${PROJECT_NAME} SHARED
    "${CMAKE_SOURCE_DIR}/src/register_types.cpp"
    "${CMAKE_SOURCE_DIR}/src/register_types.h"
)

target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_20)

target_link_libraries(${PROJECT_NAME} PRIVATE gdtemplate_game)

# Must match the library paths in godot/bin/gdtemplate.gdextension.
set(GDEXTENSION_BIN_DIR "${CMAKE_SOURCE_DIR}/godot/bin")

set_target_properties(${PROJECT_NAME} PROPERTIES
    OUTPUT_NAME "gdtemplate"
    DEBUG_POSTFIX ".debug"
    RUNTIME_OUTPUT_DIRECTORY "${GDEXTENSION_BIN_DIR}"
    LIBRARY_OUTPUT_DIRECTORY "${GDEXTENSION_BIN_DIR}"
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
)

# Multi-config generators append Debug/ or Release/ unless these are set too.
foreach(CONFIG IN ITEMS DEBUG RELEASE RELWITHDEBINFO MINSIZEREL)
    set_target_properties(${PROJECT_NAME} PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY_${CONFIG} "${GDEXTENSION_BIN_DIR}"
        LIBRARY_OUTPUT_DIRECTORY_${CONFIG} "${GDEXTENSION_BIN_DIR}"
        ARCHIVE_OUTPUT_DIRECTORY_${CONFIG} "${CMAKE_BINARY_DIR}/lib"
    )
endforeach()
