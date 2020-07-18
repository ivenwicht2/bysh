from typing import Union

from bysh.core.store import Store
from bysh._abstract_command import Command
from bysh.core import stdio


class Bysh:

    # The main ceval
    def __init__(self, store: Store):
        self.current_ast = None
        self.store = store

    def load_ast(self, ast):
        self.current_ast = ast

    def get_command_from_name(self, cmd: str) -> Union[Command.__class__, None]:
        return self.store.commands.get(cmd, None)

    def exec_simple_command(self, node):  # CommandNode
        cls_cmd = self.get_command_from_name(node.parts[0].word)
        if cls_cmd is None:
            self.store.stderr.write('Command not found: {}\n'.format(node.parts[0].word))
            self.store.last_return_code = 1
            return

        command = cls_cmd(stdio.get_new_std(),
                          self.store.stdout,
                          self.store.stderr,
                          _store=self.store)

        command.stdin.write('yop')  # write words, except redirections
        self.store.last_return_code = command.run() or 0

    def eval(self):
        # simple commands
        for nod in self.current_ast:
            if nod.kind == 'command':
                try:
                    self.exec_simple_command(nod)
                except Exception as e:
                    self.store.stdout.write('ERROR while executing {} {}'.format(nod, e))
                    raise

        self.current_ast = None
