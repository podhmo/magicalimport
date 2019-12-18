import os
from magicalimport import import_module


try:
    config = import_module("config.py", here=os.getcwd())
    print(config.NAME)
except Exception as e:
    print(e)
