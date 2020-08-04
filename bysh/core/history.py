

class History:
    def __init__(self):
        self.command = [""]
        self.position = 0

    def add_entry(self):
        self.command.append("")
        self.position = len(self.command)

    def go_back(self):
        if self.position - 1 >= 0 :
            self.position = self.position -1
            return self.command[self.position]
        return None
    
    def go_next(self):
        if self.position + 1 < len(self.command) :
            self.position = self.position + 1
            return self.command[self.position]
        return None