from magicalimport import import_symbol

Config = [
    import_symbol("./left/__init__.py:Config", here=__file__),
    import_symbol("./current.py:Config", here=__file__),
]
