class ComponentRegistry:
    def __init__(self):
        self.pool = {}

    def __call__(self, fn):
        self.pool[fn.__name__] = fn
        return fn


component = ComponentRegistry()
