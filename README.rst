magicalimport
========================================

Importing a module from physical file path.

examples
----------------------------------------

these files are existed, then..

.. code-block:: bash

  $ tree
  .
  ├── a
  │   └── b
  │       └── c
  │           └── foo.py
  └── main.py

  4 directories, 3 files


a/b/c/foo.py

.. code-block:: python

  name = "foo"
  _age = "*secret*"

.. code-block:: python

  from magicalimport import import_by_physical_path

  # importing foo.py as the module named foo2
  foo = import_by_physical_path("./a/b/c/foo.py", as_="foo2")
  print(foo.name)

  # cached by sys.modules, so it is ok.
  import foo2
  print(foo2.name)


star import
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from magicalimport import import_by_physical_path
   from magicalimport import expose_all_members

   # something of like a `from foo import *`
   expose_all_members(import_by_physical_path("./a/b/c/foo.py"))
   print(name)  # "foo"
   # print(_age)  # NameError.. because expose_all_members() doesn't expose the symbols started by "_"

   # or
   from magicalimport import expose_members
   expose_all_members(import_by_physical_path("./a/b/c/foo.py"), members=["_age"])
   print(_age)  # "*secret*"
