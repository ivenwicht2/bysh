from bysh._abstract_command import Command

import os
import pathlib

__command__ = 'cd'


class cd(Command):
    def __init__(self, stdin, stdout, stderr, *args, **kwargs):
        super().__init__(stdin, stdout, stderr)

        self.store = kwargs.get('_store', None)
        if self.store is None:
            raise RuntimeError('_store: Store was not given in builtin <cd> parameters')

    def run(self, *args, **kwargs) -> int:
        togo = pathlib.Path(self.stdin.readline())
        try:
            os.chdir(togo)
            self.store.path = togo  # store doesnt consider this, and sets to current path.
            return 0
        except OSError:
            self.stderr.write('Unable to cd to {}'.format(togo))
            return 1
        return 1
