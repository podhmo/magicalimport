import sys

try:
    from importlib.util import spec_from_file_location
    from importlib.util import module_from_spec

    def _create_module(module_id, path):
        spec = spec_from_file_location(module_id, path)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules[module_id] = module
        return module

except ImportError:
    # for 3.4
    from importlib import machinery

    def _create_module(module_id, path):
        return machinery.SourceFileLoader(module_id, path).load_module()
