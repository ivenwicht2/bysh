# main entry point

from bysh.shell import Shell
from bysh.core.store import Store
from bysh.core.bysh import Bysh

if __name__ == '__main__':
    # Main entry point.
    # Creates a three elements:
    #    - Store : the place where all internal and public data is stored
    #    - Bysh  : the engine, which executes commands. Relies on store for some variables
    #    - Shell : A shell, creating a loop and passing commands to the engine.
    
    # We then execute the Read Execute Print Loop of the Shell.

    s = Store()

    sh = Shell(
        Bysh(s),
        s
    )
    sh.repl_loop()
