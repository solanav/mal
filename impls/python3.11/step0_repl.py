def READ():
    return input("~> ")
    
def EVAL(exp):
    return exp
    
def PRINT(exp):
    print(exp)
    
def rep():
    try:
        while True:
            PRINT(EVAL(READ()))
    except EOFError:
        print("\nBye!")
        return
    
rep()