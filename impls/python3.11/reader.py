import re
from typing import List
from maltypes import *

MAL_TOKENS = "[\s,]*(~@|[\[\]{}()'`~^@]|\"(?:\\.|[^\\\"])*\"?|;.*|[^\s\[\]{}('\"`,;)]*)"
    
def tokenize(s: str) -> List[str]:
    return re.findall(MAL_TOKENS, s)[:-1]

class Reader:
    def __init__(self):
        self.tokens = []
        self.i = 0
    
    def next(self):
        self.i += 1
    
    def peek(self):
        return self.tokens[self.i]
            
    
    def read_str(self) -> MalType:
        self.read_line(input("~> "))
        return self.read_form()

    def read_form(self) -> MalType:
        if self.peek() == "(":
            return self.read_list()
        if self.peek() == "[":
            return self.read_vector()
        else:
            return self.read_atom()
        
    def read_line(self, line):
        self.tokens = tokenize(line)

    def read_list(self) -> MalList:
        mal_list = MalList()
        
        while True:
            try:
                t = self.peek()
            except:
                print("EOF unbalanced!")
                break
            
            if t == "(":
                self.next()
                continue
            elif t == ")":
                break
            
            f = self.read_form()
            
            mal_list.append(f)
            self.next()
        
        return mal_list

    def read_vector(self) -> MalVector:
        mal_list = MalList()
        
        while True:
            try:
                t = self.peek()
            except:
                print("EOF unbalanced!")
                break
            
            if t == "[":
                self.next()
                continue
            elif t == "]":
                break
            
            f = self.read_form()
            
            mal_list.append(f)
            self.next()
        
        return mal_list

    def read_atom(self):
        curr = self.peek()
        
        if re.match(r"(-|\+)?[0-9]+", curr):
            return MalNumber(curr)
        elif re.match(r"true", curr):
            return MalTrue()
        elif re.match(r"false", curr):
            return MalFalse()
        elif re.match(r"nil", curr):
            return MalNil()
        elif re.match(r"\"(?:\\.|[^\\\"])*\"?", curr):
            return MalString(curr)
        elif re.match(r"[^\s\[\]{}('\"`,;)]*", curr):
            return MalSymbol(curr)
        else:
            raise Exception(f"Failed to understand what {curr} is")