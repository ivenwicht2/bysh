from bysh._abstract_command import Command
import os

__command__ = 'ls'


class ls(Command):
    def __init__(self, stdin, stdout, stderr, *args, **kwargs):
        super().__init__(stdin, stdout, stderr)

        self.store = kwargs.get('_store', None)
        if self.store is None:
            raise RuntimeError('_store: Store was not given in <ls> parameters')

    def run(self, arguments, *args, **kwargs):
        try:
            dt = '\n'.join(os.listdir()) + '\n'
        except PermissionError:
            self.stderr.write('Permission denied\n')
            return 1
        self.stdout.write(dt)
        self.stdout.flush()
        return 0
