import string
import magicalimport
import sys
import os.path


string2 = magicalimport.import_module(string.__file__)
print(string == string2)

assert "urlib" not in sys.modules
urllib2 = magicalimport.import_module(
    os.path.join(os.path.dirname(string.__file__), "urllib/__init__.py")
)
import urllib  # noqa

print(urllib == urllib2)
