from magicalimport import import_from_physical_path

foo = import_from_physical_path("./a/b/c/foo.py", as_="foo2")


import foo2  # noqa: F401

print(foo2.name)
