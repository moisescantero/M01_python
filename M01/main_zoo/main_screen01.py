from colorama import init
init()

colors={
    "black":"30",
    "red":"31",
    "green":"32",
    "yellow":"33",
    "blue":"34",
    "magenta":"35",
    "cyan":"36",
    "white":"37",
    "reset":"39",    
    }

background={
    "black":"40",
    "red":"41",
    "green":"42",
    "yellow":"43",
    "blue":"44",
    "magenta":"45",
    "cyan":"46",
    "white":"47",
    "reset":"49",    
    }

styles={
    "bold": 1,
    "underline": 4,
    "blink": 5,
    "reversed": 7,    
    }



def clear():
    print("\033[2J")

def locate(line,column):  
    print("\033[{};{}H".format(line, column), end="")
      
def clearLine(line=None,column=None):
    if line is not None and column is not None:
        locate(line,column)
    elif line is not None:
        locate(line,1)
        
    print("\033[K", end="")

def processParams(params):
    if "line" in params:
        line=params["line"]
        column=1
        if "column" in params:
            column=params["column"]
        locate(line,column)
    if "colors" in params and params["colors"] in colors:
        print("\033[{}m".format(colors[params["colors"]]),end="")
    if "back" in params and params["back"] in background:
        print("\033[{}m".format(background[params["back"]]),end="")
    if "style" in params and params["style"] in colors:
        print("\033[{}m".format(style[params["style"]]),end="")
        
def Print(cadena,**params):
    processParams(params)
    
    if "nl" in params and params["nl"]:
        print(cadena)
    else:
        print(cadena, end="")
    if "nr" not in params:
        Reset()

def Input(msg, **params):
    processParams(params)
    if "dirty" not in params:
        clearLine()
    
    return input(msg)

def Format(style,colorText=37,colorBack=40):
    print("\033[{};{};{}m".format(style,colorText,colorBack),end="")

def Reset():
    Format(0)
