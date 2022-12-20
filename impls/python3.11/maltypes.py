from typing import List

class MalType:
    contents: List
    
    def __init__(self, contents):
        self.contents = contents
    
    def __str__(self) -> str:
        return str(self.contents)
    
class MalList(MalType):
    def __init__(self):
        super().__init__([])
        self.list_type = None
        
    def append(self, v):
        # if self.list_type == None:
        #     self.list_type = type(v)

        # if self.list_type != type(v):
        #     raise Exception("Lists can only have one type")

        self.contents.append(v)
    
    def __str__(self) -> str:
        return str(f"({' '.join([str(o) for o in self.contents])})")
    
class MalNumber(MalType):
    def __init__(self, v):
        super().__init__(int(v))
    
class MalVector(MalType):
    def __init__(self, s):
        super().__init__(s)
    
class MalHashmap(MalType):
    def __init__(self, s):
        super().__init__(s)
    
class MalKeyword(MalType):
    def __init__(self, s):
        super().__init__(s)
    
class MalString(MalType):
    def __init__(self, s):
        super().__init__(s)
    
class MalNil(MalType):
    def __init__(self):
        super().__init__(None)
    
class MalTrue(MalType):
    def __init__(self):
        super().__init__(True)
    
class MalFalse(MalType):
    def __init__(self):
        super().__init__(False)
    
class MalSymbol(MalType):
    def __init__(self, s):
        super().__init__(s)