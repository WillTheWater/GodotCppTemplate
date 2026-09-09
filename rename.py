#!/usr/bin/env python3
"""Rename this template to your own project. Usage: python rename.py MyGame"""

import os
import re
import shutil
import sys

OLD_LIB = "gdtemplate"
OLD_PROJECT = "godot_cpp_template"
SKIP_DIRS = {".git", "godot-cpp", "out", "build", ".vs", ".godot"}
TEXT_SUFFIXES = {".txt", ".json", ".h", ".cpp", ".gdextension", ".godot", ".md", ".py"}


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python rename.py MyGame")

    name = sys.argv[1]
    # The name becomes a C function name in entry_symbol.
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name):
        sys.exit("Name must be letters, digits and underscores, and cannot start with a digit.")

    root = os.path.dirname(os.path.abspath(__file__))
    changed = []

    for folder, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if os.path.splitext(f)[1] not in TEXT_SUFFIXES:
                continue
            path = os.path.join(folder, f)
            if os.path.samefile(path, os.path.abspath(__file__)):
                continue
            with open(path, encoding="utf-8", newline="") as fh:
                before = fh.read()
            after = before.replace(OLD_PROJECT, name).replace(OLD_LIB, name)
            if after != before:
                with open(path, "w", encoding="utf-8", newline="") as fh:
                    fh.write(after)
                changed.append(os.path.relpath(path, root))

    settings = os.path.join(root, "godot", "project.godot")
    with open(settings, encoding="utf-8", newline="") as fh:
        before = fh.read()
    after = re.sub(r'config/name=".*"', 'config/name="%s"' % name, before)
    if after != before:
        with open(settings, "w", encoding="utf-8", newline="") as fh:
            fh.write(after)
        changed.append("godot/project.godot")

    manifest = os.path.join(root, "godot", "bin", OLD_LIB + ".gdextension")
    if os.path.exists(manifest):
        os.rename(manifest, os.path.join(root, "godot", "bin", name + ".gdextension"))
        changed.append("godot/bin/%s.gdextension" % name)

    # Godot regenerates this, and a stale one collides with the renamed manifest.
    uid = manifest + ".uid"
    if os.path.exists(uid):
        os.remove(uid)

    # Both cache the old name and must be rebuilt.
    for stale in (os.path.join(root, "out"), os.path.join(root, "godot", ".godot")):
        if os.path.isdir(stale):
            shutil.rmtree(stale, ignore_errors=True)
            changed.append("removed " + os.path.relpath(stale, root))

    print("Renamed to '%s':" % name)
    for c in changed:
        print("  " + c)
    print("\nDelete rename.py, then build and open godot/project.godot.")


if __name__ == "__main__":
    main()
