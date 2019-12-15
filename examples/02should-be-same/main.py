import sys
from magicalimport import import_module

commands = import_module("./app/commands.py", here=__file__)
di = import_module("./app/di.py", here=__file__)

print(f"@! from {__name__!r} module {di.component.__module__!r}", file=sys.stderr)
print(
    "id(di.component) == id(commands.component) ?",
    id(di.component) == id(commands.component),
)
