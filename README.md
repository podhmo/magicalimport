# magicalimport

[![PyPI version](https://badge.fury.io/py/magicalimport.svg)](https://badge.fury.io/py/magicalimport)
[![Build Status](https://travis-ci.org/podhmo/magicalimport.svg?branch=master)](https://travis-ci.org/podhmo/magicalimport)

`magicalimport` is a Python library that provides a flexible way to import modules and symbols directly from their physical file paths.

## Motivation

In some cases, you might want to import a Python module that is not part of a standard package or is not located in Python's `sys.path`. For example:

*   Loading a plugin from a user-specified path.
*   Using a Python script as a configuration file.
*   Dynamically loading modules in a script or a tool.

Standard import mechanisms can be cumbersome in these scenarios. `magicalimport` simplifies this by allowing you to import modules directly using their file paths.

A key feature of this library is its special handling of `.py` files. The `import_module` function can distinguish between a regular module path (like `my_package.my_module`) and a direct file path (like `./path/to/my_module.py`), providing a unified interface for both.

## Installation

You can install `magicalimport` using pip:

```bash
pip install magicalimport
```

## Basic Usage

Let's say you have the following directory structure:

```
.
├── my_app
│   └── main.py
└── external_module
    └── helper.py
```

And `helper.py` contains:

```python
# external_module/helper.py
def greet(name):
    return f"Hello, {name}!"
```

From `main.py`, you can import `helper.py` like this:

```python
# my_app/main.py
import os
from magicalimport import import_from_physical_path

# Assuming the script is run from the project root
helper_path = os.path.abspath("../external_module/helper.py")
helper = import_from_physical_path(helper_path)

print(helper.greet("world"))
# => Hello, world!
```

## Special Handling of .py Files

The `import_module` function is a convenient wrapper that combines Python's standard `importlib.import_module` with `import_from_physical_path`. It automatically detects whether the provided path is a file path ending in `.py` or a regular module path.

```python
from magicalimport import import_module

# Imports a regular module
http_client = import_module("http.client")
print(http_client.HTTPConnection)

# Imports a .py file directly
helper = import_module("./external_module/helper.py")
print(helper.greet("again"))
```

This allows you to use the same function for both types of imports, simplifying your code.

## Importing Symbols

You can also import a specific symbol (a class, function, or variable) from a module using `import_symbol`. The symbol is specified using a string in the format `path/to/module.py:symbol_name`.

```python
from magicalimport import import_symbol

# Import the 'greet' function directly
greet_func = import_symbol("./external_module/helper.py:greet")

print(greet_func("from symbol"))
# => Hello, from symbol!

# You can also import from standard libraries
HTTPConnection = import_symbol("http.client:HTTPConnection")
print(HTTPConnection)
```

## API Reference

### `import_from_physical_path(path, as_=None, here=None, cwd=True)`

*   `path` (str): The relative or absolute path to the `.py` file.
*   `as_` (str, optional): The name for the module in `sys.modules`. If not provided, a name is generated from the file path.
*   `here` (str, optional): The base directory to resolve relative paths. If `None`, it's determined from the caller's file (`__file__`) or the current working directory.
*   `cwd` (bool): If `True` and `here` is `None`, the current working directory is used as the base.

### `import_module(module_path, here=None, cwd=True)`

*   `module_path` (str): A module path (e.g., `my_package.my_module`) or a file path (e.g., `./my_module.py`).
*   `here`, `cwd`: Same as in `import_from_physical_path`.

### `import_symbol(sym, here=None, sep=":")`

*   `sym` (str): The string representing the symbol to import, in the format `<module_path>:<symbol_name>`.
*   `here`: Same as above.
*   `sep` (str): The separator between the module path and the symbol name.

### `expose_all_members(module)`

*   Imports all members (that don't start with `_`) from the given module into the caller's global scope, similar to `from module import *`.

### `expose_members(module, members)`

*   Imports specified `members` from the given `module` into the caller's global scope.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
