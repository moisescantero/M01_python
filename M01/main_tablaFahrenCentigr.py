"""TABLA DE CONVERSIÓN CENTÍGRADOS A FAHRENHEIT Y VICEVERSA"""
"""le pedimos 'c' o 'f' al usuario y aplicamos fórmula de con-
versión para imprimir una tabla de centig a farenh o viceversa"""
"""C=(F-32)*5/9      F=(C*9/5)+32    FÓRMULAS DE CONVERSIÓN"""

def FahrToCent(g):
    return(g-32)*5/9
def CentToFahr(g):
    return(g*9/5)+32

def centigrados(ini,fin):
    for grados in range(0,240,10):
        print("{}ºF -> {}ºC".format(grados,FahrToCent(grados),2))
def fahrenheit(ini,fin):
    for grados in range(0,110,10):
        print("{}ºC -> {}ºF".format(grados,CentToFahr(grados),2))

tipo=input("Salida (F/C): ")

if tipo== 'C':
    centigrados(0,230)
elif tipo=='F':
    fahrenheit(0,100)
else:
    print("Tipo incorrecto")