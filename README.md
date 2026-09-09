# Godot C++ Template

Blank Godot 4.7 project with a C++ GDExtension.

Requires CMake 3.21 or newer, a C++20 compiler, and Python 3.

## 1. Clone

```
git clone --recurse-submodules https://github.com/WillTheWater/GodotCppTemplate.git MyGame
cd MyGame
```

`MyGame` is your project name.

## 2. Rename

`rename.py` Setup helper to rename the template for your own project.

```
python rename.py MyGame
```

Rewrites the library name, entry symbol, manifest filename, CMake
project and the Godot project name.

## 3. Build

```
cmake --preset default
cmake --build --preset debug
```

The first command configures the build. The second compiles the extension.

The editor loads the debug library. 
Exports needs the release build, so build it before exporting the release

```
cmake --build --preset release
```

## 4. Open

Open `godot/project.godot` in Godot. Press F5, the output panel should print
`Hello from C++`.


## Notes

How to add new classes:

- Put the header and source in `src/game/`, like `Example.h/cpp`.
- Add both to `SOURCES` and `HEADERS` in `src/game/CMakeLists.txt`.
- Register the class in `RegisterGameTypes.cpp`.
- Rename the template namespace to your preference in `RegisterGameTypes.h/cpp` & `register_types.cpp`.

Rebuilding while the editor is open reloads the extension. 
Changing the entry symbol or the manifest requires restarting.
