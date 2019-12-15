import sys
from magicalimport import import_symbol

component = import_symbol("di.py:component", here=__file__)


@component
def db():
    return DB()


class DB:
    pass


print(f"@@ from {__name__!r} module {component.__module__!r}", file=sys.stderr)
