from colorama import init
init()
def clear():
    print("\033[2J")

def locate(line,column):  
    print("\033[{};{}H".format(line, column), end="")
      
def clearLine():
    print("\033[K", end="")

def Print(cadena,line,column, delEnd):
    locate(line,column)
    if delEnd:
        clearLine()
    print(cadena, end="")

def Input(msg, line, column, delEnd):
    locate(line, column)
    if delEnd:
        clearLine()
    return input(msg)