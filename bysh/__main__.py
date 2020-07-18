# main entry point

from bysh.shell import Shell
from bysh.core.store import Store
from bysh.core.bysh import Bysh

if __name__ == '__main__':

    s = Store()

    sh = Shell(
        Bysh(s),
        s
    )
    sh.repl_loop()
