import sys

__ALL__ = [
    "import_module",
    "_create_module",
    "ModuleNotFoundError",
    "FileNotFoundError",
]


from importlib import import_module  # NOQA
from importlib.util import spec_from_file_location
from importlib.util import module_from_spec

def _create_module(module_id, path):
    spec = spec_from_file_location(module_id, path)
    module = module_from_spec(spec)
    sys.modules[module_id] = module
    spec.loader.exec_module(module)
    return module


# ModuleNotFoundError is built-in in Python 3.6+
# FileNotFoundError is built-in in Python 3.3+

try:
    # Python 3.6+
    _ModuleNotFoundError = ModuleNotFoundError
except NameError:
    class _ModuleNotFoundError(ImportError):  # type: ignore
        pass
ModuleNotFoundError = _ModuleNotFoundError

try:
    # Python 3.3+
    _FileNotFoundError = FileNotFoundError
except NameError:
    class _FileNotFoundError(IOError):  # type: ignore
        pass
FileNotFoundError = _FileNotFoundError
