import sys

from bysh.lib import bashlex
from bysh.lib import colorama

from bysh.core import Bysh
from bysh.core.store import Store
from bysh.core.history import History

from msvcrt import getch


class Shell:

    def __init__(self, bysh: Bysh, store: Store):

        self.store = store
        self.bysh = bysh

        self.current_input: str = ''  # last command
        self.current_ast = None       # AST of this command

        self.position_in_input = 0

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
        self.History = History()

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
                continue

            if self.tmp_input == b"\x00" :
                self.tmp_input = getch()
                self.special_caractere[self.tmp_input]()
                continue

            if self.tmp_input == b'\b' or self.tmp_input == b'\t':
                self.special_caractere[self.tmp_input]()
                continue
            
            self.current_input += str(self.tmp_input.decode('utf-8'))

            self.fwrite(self.current_input[-len(self.tmp_input)])
            self.History.command[-1] = self.current_input.strip()

        self.current_input = self.current_input.strip()

        if not self.current_input.isspace() and self.current_input != "": 
            self.History.add_entry()
        self.History.position = len(self.History.command)-1

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
    
    def del_command(self):
        lenght = len(self.current_input)
        self.fwrite("\b"*lenght)
        self.fwrite(" "*lenght)
        self.fwrite("\b"*lenght)

    def autocomplete(self):
        pass

    def erase_cacatere(self):
        if len(self.current_input) > 0 :
            self.current_input = self.current_input[:-1]
            self.fwrite('\b \b')
        

    def left_arrow(self):
        self.fwrite('\b')

    def down_arrow(self):
        new_entry = self.History.go_next()
        if new_entry != None : 
            self.del_command()
            self.current_input = new_entry 
            self.fwrite(self.current_input)

    def right_arrow(self):  
        pass

    def up_arrow(self):
        new_entry = self.History.go_back()
        if new_entry != None : 
            self.del_command()
            self.current_input = new_entry 
            self.fwrite(self.current_input)

    def insert(self):
        pass

    def delete(self):
        pass

    def new_input(self,current_input):
        tmp = list(self.current_input)
        tmp.insert(self.position_in_input,current_input)
        self.current_input = "".join(tmp) 
        self.position_in_input += len(current_input)
