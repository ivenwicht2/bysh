import typing

__command__ = ''


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

    def run(self, arguments, *args, **kwargs) -> int:
        raise NotImplementedError
