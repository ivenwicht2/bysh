import sys

from bysh.core import Bysh
from bysh.lib import bashlex
from bysh.lib import colorama

from bysh.core.store import Store


class Shell:

    def __init__(self, bysh: Bysh, store: Store):

        self.store = store
        self.bysh = bysh

        self.current_input: str = ''
        self.current_ast = None

    def repl_loop(self):
        while not self.store.exit:
            self.get_input()
            if not self.current or self.current_input.isspace():
                continue

            self.parse_ast(self.current_input)

            # [print(a.dump()) for a in self.current_ast]
            self.bysh.load_ast(self.current_ast)
            self.bysh.eval()

    def get_input(self):
        self.store.stdout.write(self.store.ps1)
        self.store.stdout.flush()
        self.current_input = self.store.stdin.readline()

    def parse_ast(self, src: str):
        self.current_ast = bashlex.parse(src)
