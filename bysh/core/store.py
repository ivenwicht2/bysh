import sys
import os
import importlib
import pathlib
import getpass
import platform

from bysh.lib import colorama


class Store:

    def __init__(self):

        colorama.init()
        self.commands = {}

        # Store to handle all variables, their getters and setters
        self._path = pathlib.Path().absolute()
        self.user = getpass.getuser()
        self.host = platform.uname().node

        self.stdin = sys.stdin
        self.stdout = sys.stdout
        self.stderr = sys.stderr

        self._ps1 = (
                colorama.Fore.GREEN
                + '{user}@{host}'
                + colorama.Fore.BLUE
                + ':{path}$'
                + colorama.Fore.RESET
                + ' '
        )
        self.ps2 = ''
        self.ps3 = ''
        self.ps4 = ''
        self.last_return_code = 0  # $?

        self.load_commands()

    def load_commands(self, folder=None):
        # load commands in bysh.builtins, and bysh.commands
        if folder is None:
            self.load_commands('builtins')
            self.load_commands('commands')
        else:
            importlib.invalidate_caches()
            # TODO: folder structure is hardcoded here
            cmds = [f for f in os.listdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), folder))
                    if (f.endswith('.py') and not f.startswith('_'))]
            for f in cmds:
                mod = importlib.import_module('.' + f[:-3], 'bysh.{}'.format(folder))
                cmd = getattr(mod, mod.__command__)
                self.commands[mod.__command__] = cmd

                if getattr(cmd, 'alias', None):
                    for a in getattr(cmd, 'alias'):
                        self.commands[a] = cmd
    @property
    def ps1(self):
        return self._ps1.format_map({'path': self.path,
                                     'user': self.user,
                                     'host': self.host})  # cannot use self.__dict__ anymore because of property

    @ps1.setter
    def ps1(self, value):
        self._ps1 = value

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, _):
        self._path = pathlib.Path().absolute()
