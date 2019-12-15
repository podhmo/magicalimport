import logging
import os.path
import sys
from magicalimport.compat import ModuleNotFoundError
from magicalimport.compat import FileNotFoundError
from magicalimport.compat import _create_module
from magicalimport.compat import import_module as import_module_original

logger = logging.getLogger(__name__)


def expose_all_members(module, globals_=None, _depth=2):
    members = {k: v for k, v in module.__dict__.items() if not k.startswith("_")}
    return expose_members(module, members, globals_=globals_, _depth=_depth)


def expose_members(module, members, globals_=None, _depth=1):
    if globals_ is None:
        frame = sys._getframe(_depth)
        globals_ = frame.f_globals
    globals_.update({k: module.__dict__[k] for k in members})
    return globals_


def _module_id_from_path(path):
    logger.debug("	-> %s (path)", path)

    dirname = os.path.dirname(path)
    basename = os.path.basename(path)

    module_id = "{}.{}".format(dirname.replace("/", "_"), basename.rsplit(".py", 1)[0])
    logger.debug("	<- %s (module_id)", module_id)
    return module_id


_FAILED = set()  # singleton


def import_from_physical_path(path, as_=None, here=None):
    global _failed

    if here is not None:
        here = here if os.path.isdir(here) else os.path.dirname(here)
        here = os.path.abspath(here)
        path = os.path.normpath(os.path.join(here, path))

    module_id = as_ or _module_id_from_path(path)
    if module_id in sys.modules:
        return sys.modules[module_id]

    syspath_list = [os.getcwd()]
    syspath_list.extend(sys.path)
    for syspath in syspath_list:
        if not path.startswith(syspath):
            continue

        guessed_module = path[len(syspath) :].lstrip("/").rsplit(".py", 1)[0]
        if guessed_module in _FAILED:
            continue

        try:
            return import_module_original(guessed_module)
        except ImportError:
            _FAILED.add(guessed_module)
            pass

    if "." in module_id and as_ is None:
        parent_module_id = module_id.rsplit(".")[0]
        if parent_module_id not in sys.modules:
            init_py = os.path.join(os.path.dirname(path), "__init__.py")
            if os.path.exists(init_py):
                _create_module(parent_module_id, init_py)
            else:
                # TODO: don't have to create __init__.py
                try:
                    with open(init_py, "w"):
                        pass
                    _create_module(parent_module_id, init_py)
                    # # xxx: using fake module as parent module
                    # import magicalimport._fake as fake_module

                    # parent_module = _create_module(parent_module_id, fake_module.__file__)
                    # parent_module.__file__ = init_py
                except PermissionError as e:
                    module_id = module_id.replace(".", "_")
                    logger.warn(
                        "open %s, cannot accessable (%r). new module_id is %r",
                        init_py,
                        e,
                        module_id,
                    )

    try:
        return _create_module(module_id, path)
    except (FileNotFoundError, OSError) as e:
        raise ModuleNotFoundError(e)


def import_module(module_path, here=None, sep=":"):
    _, ext = os.path.splitext(module_path)
    if ext == ".py":
        m = import_from_physical_path(module_path, here=here)
        logger.debug("import module %s", m)
        return m
    else:
        try:
            return import_module_original(module_path)
        except ImportError as e:
            if ImportError.__module__ == ModuleNotFoundError.__module__:
                raise
            raise ModuleNotFoundError(e)


def import_symbol(sym, here=None, sep=":", ns=None, silent=False):
    if ns is not None and sep not in sym:
        sym = "{}{}{}".format(ns, sep, sym)
    module_path, fn_name = sym.rsplit(sep, 2)
    try:
        module = import_module(module_path, here=here, sep=sep)
    except (
        ImportError,
        ModuleNotFoundError,
    ) as e:  # ModuleNotFoundError is subclass of ImportError
        if not silent:
            sys.stderr.write("could not import {!r}\n{}\n".format(sym, e))
        raise
    try:
        return getattr(module, fn_name)
    except AttributeError as e:
        if not silent:
            sys.stderr.write("could not import {!r}\n{}\n".format(sym, e))
        raise ImportError(e)
