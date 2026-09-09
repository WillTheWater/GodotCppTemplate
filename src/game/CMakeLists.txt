set(SOURCES
    "src/Example.cpp"
    "src/RegisterGameTypes.cpp"
)
set(HEADERS
    "include/game/Example.h"
    "include/game/RegisterGameTypes.h"
)

add_library(gdtemplate_game STATIC ${SOURCES} ${HEADERS})

# PRIVATE src/ keeps implementation headers out of reach of other modules.
target_include_directories(gdtemplate_game
    PUBLIC  "${CMAKE_CURRENT_SOURCE_DIR}/include"
    PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/src"
)

# PUBLIC because these headers expose godot-cpp types.
target_link_libraries(gdtemplate_game PUBLIC godot::cpp)

target_compile_features(gdtemplate_game PUBLIC cxx_std_20)
