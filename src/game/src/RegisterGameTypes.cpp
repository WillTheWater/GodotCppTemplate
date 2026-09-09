#include "game/RegisterGameTypes.h"

#include <godot_cpp/core/class_db.hpp>

#include "game/Example.h"

namespace Template
{
    void RegisterGameTypes()
    {
        GDREGISTER_CLASS(Example);
    }
}
