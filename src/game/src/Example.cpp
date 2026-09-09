#include "game/Example.h"

#include <godot_cpp/core/class_db.hpp>
#include <godot_cpp/variant/utility_functions.hpp>

using namespace godot;

Example::Example() {}

Example::~Example() {}

void Example::_ready()
{
    // Also fires in the editor; GDREGISTER_RUNTIME_CLASS would prevent that.
    UtilityFunctions::print(Greeting);
}

void Example::SetGreeting(const String& NewGreeting) { Greeting = NewGreeting; }

String Example::GetGreeting() const { return Greeting; }

void Example::_bind_methods()
{
    ClassDB::bind_method(D_METHOD("SetGreeting", "NewGreeting"), &Example::SetGreeting);
    ClassDB::bind_method(D_METHOD("GetGreeting"), &Example::GetGreeting);

    ADD_PROPERTY(PropertyInfo(Variant::STRING, "Greeting"), "SetGreeting", "GetGreeting");
}
