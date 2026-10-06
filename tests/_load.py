"""Load a script from a CoreReplica skill folder (folder names have hyphens)."""

import importlib.util
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(folder, name):
    path = os.path.join(ROOT, "skills", folder, "scripts", name + ".py")
    spec = importlib.util.spec_from_file_location("corereplica_" + name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
