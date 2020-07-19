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

    def run(self, arguments, *args, **kwargs) -> int:
        togo = self.store.home
        if len(arguments) > 1:
            # cmdname + args
            togo = pathlib.Path(arguments[1])
        try:
            os.chdir(togo)
            self.store.path = togo  # store doesnt consider this, and sets to current path.
            return 0
        except FileNotFoundError:
            self.stderr.write('No such file or directory\n')
            return 1
        except PermissionError:
            self.stderr.write('Permission denied\n')
            return 1
        except NotADirectoryError:
            self.stderr.write('Not a directory\n')
            return 1
        except OSError:
            self.stderr.write('Unable to cd to {}\n'.format(togo))
            return 1
        return 1
