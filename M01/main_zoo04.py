
"""programa de un zoo que pide edad para calcular el
precio total de todas ellas cuando metamos un "0" para
salir validando que la edad solo sean enteros positivos,
además tenemos un módulo creado por mí para posicionar
el cursor y mejorar la presentación en pantalla"""
import main_zooPantalla01
from colorama import init
init()


def calcularPrecioEntrada(e):
    if e>0 and e<=2:
        precio=0
    elif e<=12:
        precio=14
    elif e<65:
        precio=23
    else:
        precio=18
        
    return precio

def validaEdad(cadena):#validar que solo acepte positivos
    try:
        n = int(cadena)
        if n>= 0:#entonces el valor es válido
            return True
        return False
    except:
        return False
    
def pedirEdad():
    main_zooPantalla01.locate(1,1)
    edad = input("¿Qué edad tienes?: ")
    while validaEdad(edad) == False:
        print("Edad inválida.")
        main_zooPantalla01.locate(1,1)
        edad = input("¿Qué edad tienes?: ")
    
    return int(edad)

main_zooPantalla01.clear()
edad=pedirEdad()
precioTotal = 0
linea=4

numEntradasB=0
numEntradasN=0
numEntradasA=0
numEntradasJ=0

while edad != 0:
    precioE = calcularPrecioEntrada(edad)
    if precioE == 0:
        linea=4
        numEntradasB+=1
        main_zooPantalla01.locate(linea,1)
        linea+=1
        print("\tPrecio Entrada: {}\tNum. Entradas: {}".format(precioE,numEntradasB))
    
    if precioE == 14:
        linea=5
        numEntradasN+=1
        main_zooPantalla01.locate(linea,1)
        linea+=1
        print("\tPrecio Entrada: {}\tNum. Entradas: {}".format(precioE,numEntradasN))
    
    if precioE == 23:
        linea=6
        numEntradasA+=1
        main_zooPantalla01.locate(linea,1)
        linea+=1
        print("\tPrecio Entrada: {}\tNum. Entradas: {}".format(precioE,numEntradasA))
    
    if precioE ==18:
        linea=7
        numEntradasJ+=1
        main_zooPantalla01.locate(linea,1)
        linea+=1
        print("\tPrecio Entrada: {}\tNum. Entradas: {}".format(precioE,numEntradasJ))
    

    precioTotal += precioE    
    edad=pedirEdad()

main_zooPantalla01.locate(linea,1)
print("\tTotal: {}".format(precioTotal))

