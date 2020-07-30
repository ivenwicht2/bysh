import sys

from bysh.lib import bashlex
from bysh.lib import colorama

from bysh.core import Bysh
from bysh.core.store import Store

from msvcrt import getch


class Shell:

    def __init__(self, bysh: Bysh, store: Store):

        self.store = store
        self.bysh = bysh

        self.current_input: str = ''  # last command
        self.current_ast = None       # AST of this command

        self.special_caractere = {
            b'\t' : self.autocomplete,
            b'\b' : self.erase_cacatere,
            b'K' :  self.left_arrow,
            b'P' :  self.down_arrow,
            b'M' :  self.right_arrow,
            b'H' :  self.up_arrow,
            b'R' :  self.insert,
            b'S' :  self.delete
        }

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
            self.bysh.load_ast(self.current_ast)
            self.bysh.eval()

    def get_input(self) -> None:
        """
        Get input from store.stdin, and store it in self.current_input
        :return:
        """
        self.fwrite(self.store.ps1)
        
        self.current_input = ""
        self.tmp_input = "" 
        
        while self.tmp_input != b"\r" :
            
            self.tmp_input = getch() 
            
            if self.tmp_input == b'\r':
                break

            if self.tmp_input == b"\x00" :
                self.tmp_iput = getch()
                self.special_caractere[self.tmp_input]()
                continue

            if self.tmp_input == b'\b' or self.tmp_input == b'\t':
                self.special_caractere[self.tmp_input]()
                continue
            
            self.current_input += str(self.tmp_input.decode('utf-8'))
            self.fwrite(self.current_input[-len(self.tmp_input)])


        self.current_input = self.current_input.strip()
        self.fwrite('\n')

    def parse_ast(self, src: str) -> None:
        """
        Parse the given command (in str), and store it in self.current_ast
        :param src:
        :return:
        """
        self.current_ast = bashlex.parse(src)

    def fwrite(self,output):
        self.store.stdout.write(output)
        self.store.stdout.flush()
    
    def autocomplete(self):
        pass

    def erase_cacatere(self):
        if len(self.current_input) > 0 :
            self.current_input = self.current_input[:-1]
            self.fwrite('\b \b')
        

    def left_arrow(self):
        pass

    def down_arrow(self):
        pass

    def right_arrow(self):  
        pass

    def up_arrow(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass