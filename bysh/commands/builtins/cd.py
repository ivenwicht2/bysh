from bysh.commands._abstract_command import Command

import os
import pathlib

__command__ = 'cd'


class cd(Command):
    def __init__(self, stdin, stdout, stderr, *args, **kwargs):
        super().__init__(stdin, stdout, stderr)

        self.store = kwargs.get('_store', None)
        if self.store is None:
            raise RuntimeError('_store: Store was not given in builtin <cd> parameters')

        self.argparser.prog = __command__
        self.argparser.add_argument('directory', help='directory to navigate', nargs='?',
                                    default=self.store.home)

    def run(self, arguments, *args, **kwargs) -> int:

        if self.parse_input(arguments[1:]):
            return 1
        try:
            os.chdir(pathlib.Path(self.arguments.directory))
            self.store.path = self.arguments.directory  # store doesnt consider this, and sets to current path.
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
            self.stderr.write('Unable to cd to {}\n'.format(self.arguments.directory))
            return 1
        return 1
