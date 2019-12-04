from magicalimport import import_module
conf = import_module("./conf/__init__.py", here=__file__)
print(conf.foo.NAME)
