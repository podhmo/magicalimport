from magicalimport import import_module

try:
    config = import_module("config.py", here=__file__)
    print(config.NAME)
except Exception as e:
    print(e)
