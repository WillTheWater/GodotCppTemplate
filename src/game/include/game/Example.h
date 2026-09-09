#pragma once

#include <godot_cpp/classes/node.hpp>

// Delete this class and its entries in CMakeLists.txt and RegisterGameTypes.cpp.
class Example : public godot::Node
{
    GDCLASS(Example, godot::Node)

public:
    Example();
    ~Example();

    void _ready() override;

    void SetGreeting(const godot::String& NewGreeting);
    godot::String GetGreeting() const;

protected:
    static void _bind_methods();

private:
    godot::String Greeting = "Hello from C++";
};
