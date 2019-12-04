from magicalimport import import_module

sub = import_module("./conf/sub/hello.py", here=__file__)
print(sub.NAME)
print(sub.INIT)
print(sub.ROOT)
