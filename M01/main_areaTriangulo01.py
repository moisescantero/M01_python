import sys

def area(b,h):
    return b*h/2
if __name__== "__main__":#nombre es el de programa principal entra y hace el bucle
    if len(sys.argv)>=3:
        base=float(sys.argv[1])
        altura=float(sys.argv[2])
    else:
        base=float(input("Base: "))
        altura=float(input("Altura: "))

    
    print("Superficie: {}".format(area(base,altura)))

