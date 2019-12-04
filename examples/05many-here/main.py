from magicalimport import import_symbol

print(import_symbol("conf/__init__.py:Config", here=__file__))
import sys

modules = []
for name in sys.modules.keys():
    if "@" in name:
        print(name)
        modules.append(name)
assert len(modules) == len(["conf", "conf/left", "conf/current"])
