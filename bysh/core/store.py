import sys
import pathlib
import getpass
import platform

from bysh.lib import colorama


class Store:

    def __init__(self):
        # Store to handle all variables, their getters and setters
        self.path = pathlib.Path().absolute()
        self.user = getpass.getuser()
        self.host = platform.uname().node

        self._ps1 = (
                colorama.Fore.GREEN
                + '{user}@{host}'
                + colorama.Fore.BLUE
                + ':{path}$'
                + colorama.Fore.RESET
                + ' '
        )
        self.ps2 = ">"

    @property
    def ps1(self):
        return self._ps1.format_map(self.__dict__)  # security expert

    @ps1.setter
    def ps1(self, value):
        self._ps1 = value
