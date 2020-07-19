import typing
import argparse

__command__ = ''


class ParsingError(Exception):
    pass


class Command:
    # base class for all commands and builtins
    def __init__(self,
                 stdin: typing.TextIO,
                 stdout: typing.TextIO,
                 stderr: typing.TextIO,
                 *args, **kwargs):
        self.stdin: typing.TextIO = stdin
        self.stdout: typing.TextIO = stdout
        self.stderr: typing.TextIO = stderr

        self.argparser = argparse.ArgumentParser(prog='CMD', add_help=False)
        self.argparser.add_argument('-h', '--help', help='show this help message and exit', action='store_true')
        self.argparser.exit = self.exit
        self.arguments = None

    def run(self, arguments, *args, **kwargs) -> int:
        raise NotImplementedError

    def parse_input(self, argus):
        # the return does not mean error, but asks to exit program.
        # used as a way to bubble exit to subclass
        try:
            self.arguments = self.argparser.parse_args(argus)
        except ParsingError:
            return 1
        if self.arguments.help:
            self.argparser.print_help(self.stdout)
            return 1
        return 0

    def exit(self, *args, **kwargs):
        raise ParsingError
