from bysh.core.store import Store


class Bysh:

    # The main ceval
    def __init__(self, store: Store):
        self.current_ast = None
        self.store = store

    def load_ast(self, ast):
        self.current_ast = ast

    def eval(self):
        self.current_ast = None
