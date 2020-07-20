import io
import typing


def get_new_std() -> typing.TextIO:
    return io.StringIO()


def get_stds() -> (typing.TextIO, typing.TextIO, typing.TextIO):
    return (
        io.StringIO(),
        io.StringIO(),
        io.StringIO()
    )


def close_stds(*stds) -> None:
    [std.close() for std in stds]
