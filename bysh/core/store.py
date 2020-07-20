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
        self._commands = {}

        # Store to handle all variables, their getters and setters
        self._path = pathlib.Path().absolute()
        self.user = getpass.getuser()
        self.host = platform.uname().node

        self.stdin = sys.stdin
        self.stdout = sys.stdout
        self.stderr = sys.stderr

        self.exit = False  # main loop

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

    def _load_commands(self, folder=None):
        # load commands in bysh.builtins, and bysh.commands
        if folder is None:
            base = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'commands')
            for d in os.listdir(base):
                if os.path.isdir(os.path.join(base, d)):
                    self._load_commands(d)

        else:
            importlib.invalidate_caches()
            # TODO: folder structure is hardcoded here
            cmds = [
                f for f in os.listdir(
                    os.path.join(
                        os.path.join(
                            os.path.dirname(
                                os.path.dirname(__file__)
                            ), 'commands'), folder)
                )
                if (f.endswith('.py') and not f.startswith('_'))
            ]
            for f in cmds:
                mod = importlib.import_module('.' + f[:-3], 'bysh.commands.{}'.format(folder))
                cmd = getattr(mod, mod.__command__, None)
                if cmd is None:
                    continue  # ignore .py if __command__ is not defined
                cmd.origin = folder
                self._commands[mod.__command__] = cmd

                if getattr(cmd, 'alias', None):
                    for a in getattr(cmd, 'alias'):
                        self._commands[a] = cmd

    @property
    def commands(self):
        if not self._commands:
            self._load_commands()
        return self._commands

    @commands.setter
    def commands(self, _):
        self._commands = {}

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

    @property
    def home(self) -> pathlib.Path:
        return pathlib.Path.home()
