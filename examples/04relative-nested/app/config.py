from . import shapes  # this is OK

# "import shapes" is NG, because this module not in sys.path
# ModuleNotFoundError: No module named 'shapes'
# see also: ../../03relative/config.py

config = shapes.Config(host="localhost", port=44444)
