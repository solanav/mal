from reader import Reader

def READ(r):
    r = Reader()
    return r.read_str()
    
def EVAL(exp):
    return exp
    
def PRINT(exp):
    print(exp)
    
def rep():
    r = Reader()
    
    while True:
        try:
            line = READ(r)
        except EOFError:
            print("\nBye!")
            return

        res = EVAL(line)
        PRINT(res)
    
rep()