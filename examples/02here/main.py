from magicalimport import import_module

conf = import_module("./conf.py", here=__file__)
print(conf.NAME)
