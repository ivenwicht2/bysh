from bysh._abstract_command import Command
import os

__command__ = 'ls'


class ls(Command):
    def __init__(self, stdin, stdout, stderr, *args, **kwargs):
        super().__init__(stdin, stdout, stderr)

        self.store = kwargs.get('_store', None)
        if self.store is None:
            raise RuntimeError('_store: Store was not given in <ls> parameters')

    def run(self, *args, **kwargs):
        self.stdout.write('\n'.join(os.listdir()) + '\n')
        self.stdout.flush()
