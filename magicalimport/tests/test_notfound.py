import unittest
import os.path

here = os.path.dirname(os.path.abspath(__file__))


class Tests(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from magicalimport import import_from_physical_path

        return import_from_physical_path(*args, **kwargs)

    def test_target_file_is_notfound(self):
        import random

        path = os.path.join(here, "missing{}.py".format(random.random()))
        with self.assertRaises(ModuleNotFoundError):
            self._callFUT(path)

    def test_target_module_is_notfound(self):
        import random

        path = os.path.join(here, "missing{}".format(random.random()))
        with self.assertRaises(ModuleNotFoundError):
            self._callFUT(path)

    # def test_target_file_has_not_member(self):
    #     import random

    #     path = os.path.join(here, "missing{}.py".format(random.random()))
    #     with self.assertRaises(ModuleNotFoundError):
    #         self._callFUT(path)
