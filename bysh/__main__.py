# main entry point

from bysh import Shell


def console_run():
    # Main entry point.

    #    - Shell : A shell, creating a loop and passing commands to the engine.

    # We then execute the Read Execute Print Loop of the Shell.

    # TODO: Some of the store's variables should be in Shell

    Shell().repl_loop()


if __name__ == '__main__':
    console_run()
