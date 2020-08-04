from bysh.lib import bashlex

from bysh.core import Engine


class Shell:

    def __init__(self):

        self.engine = Engine()
        self.store = self.engine.store

        self.current_input: str = ''  # last command
        self.current_ast = None  # AST of this command

    def repl_loop(self) -> None:
        """
        Main Read Execute Print Loop of the program
        Get input, parse it and feed the engine.
        :return: None
        """
        while not self.store.exit:
            self.get_input()

            if not self.current_input or self.current_input.isspace():
                continue

            self.parse_ast(self.current_input)

            # [print(a.dump()) for a in self.current_ast]
            self.engine.load_ast(self.current_ast)
            self.engine.eval()

    def get_input(self) -> None:
        """
        Get input from store.stdin, and store it in self.current_input
        :return:
        """
        self.store.stdout.write(self.store.ps1)
        self.store.stdout.flush()
        self.current_input = self.store.stdin.readline()

    def parse_ast(self, src: str) -> None:
        """
        Parse the given command (in str), and store it in self.current_ast
        :param src:
        :return:
        """
        try:
            self.current_ast = bashlex.parse(src)
        except bashlex.errors.ParsingError:
            self.current_ast = None
            self.store.stderr.write('Failed to parse command\n')
            self.store.stderr.flush()
