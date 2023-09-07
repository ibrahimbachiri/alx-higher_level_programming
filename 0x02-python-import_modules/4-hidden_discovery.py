#!/usr/bin/python3
import dis
import sys
import importlib.util

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <module_name.pyc>".format(sys.argv[0]))
        sys.exit(1)

    module_path = sys.argv[1]
    spec = importlib.util.spec_from_file_location("hidden_module", module_path)
    hidden_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_module)

    names = [name for name in dir(hidden_module) if not name.startswith("__")]

    for name in sorted(names):
        print(name)
