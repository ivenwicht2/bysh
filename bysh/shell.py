import sys

from bysh.core import Bysh
from bysh.lib import bashlex
from bysh.lib import colorama

from bysh.core.store import Store


class Shell:

    def __init__(self, bysh: Bysh, store: Store):
        colorama.init()
        self.stdin = sys.stdin
        self.stdout = sys.stdout
        self.stderr = sys.stderr

        self.store = store
        self.bysh = bysh

        self.current_input: str = ''
        self.current_ast = None

    def repl_loop(self):
        while True:
            self.get_input()
            self.parse_ast(self.current_input)

            if __debug__:
                [print(a.dump()) for a in self.current_ast]

    def get_input(self):
        self.stdout.write(self.store.ps1)
        self.stdout.flush()
        self.current_input = self.stdin.readline()

    def parse_ast(self, src: str):
        self.current_ast = bashlex.parse(src)
