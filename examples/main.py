from magicalimport import import_by_physical_path

foo = import_by_physical_path("./a/b/c/foo.py", as_="foo2")
print(foo.name)


import foo2
print(foo2.name)
