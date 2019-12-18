from magicalimport import import_from_physical_path

foo = import_from_physical_path("../a/b/c/foo.py")
print(foo.name)
foo = import_from_physical_path("../a/b/c/foo.py", here=__file__)
print(foo.name)
