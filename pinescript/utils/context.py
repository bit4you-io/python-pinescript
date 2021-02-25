from contextvars import ContextVar, copy_context

class context:
    strategy = ContextVar('strategy')

    def set(name, val):
        ContextVar(name).set(val)

    def copy():
        return copy_context()