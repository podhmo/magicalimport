import sys
import logging
from magicalimport import import_symbol

logging.basicConfig(level=logging.DEBUG)


print(import_symbol("conf/__init__.py:Config", here=__file__))

modules = []
for name in sys.modules.keys():
    if "@" in name:
        print(name)
        modules.append(name)
assert len(modules) == len(["conf", "conf/left", "conf/current"])
