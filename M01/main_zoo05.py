"""programa de un zoo que pide edad para calcular el
precio total de todas ellas cuando metamos un "0" para
salir validando que la edad solo sean enteros positivos,
además tenemos un módulo creado por mí para posicionar
el cursor y mejorar la presentación en pantalla,
calculo tipo de entrada según edad, saco precio según
tipo de entrada, he creado una pequeña interfaz gráfica
para presentar los datos calculados y que se actualizan
en tiempo real """
import main_zooPantalla01
from colorama import init
init()

preciosE = {#diccionario para calcular datos
        "Bebé":0.0,
        "Niñ@":14.0,
        "Adult@":23.0,
        "Jubilad@":18.0    
    }

numEntradas = {"Bebé":0,"Niñ@":0,"Adult@":0,"Jubilad@":0,}#diccionario para calcular datos

entradasQ= {#diccionario de diccionarios para presentar datos
        "Bebé": {
            "cantidad":(5,15),
            "precioA": (5,19),
            },
        "Niñ@": {
            "cantidad":(6,15),
            "precioA": (6,19),
            },
        "Adult@": {
            "cantidad":(7,15),
            "precioA": (7,19),
            },
        "Jubilad@": {
            "cantidad":(8,15),
            "precioA": (8,19),
            }
    }

def tipoEntrada(e):#funcion
    if e>0 and e<=2:
        tipo = "Bebé"
    elif e<=12:
        tipo = "Niñ@"
    elif e<65:
        tipo = "Adult@"
    else:
        tipo = "Jubilad@"
        
    return tipo

def validaEdad(cadena):#validar que solo acepte positivos
    try:
        n = int(cadena)
        if n>= 0:#entonces el valor es válido
            return True
        return False
    except:
        return False
    
def pedirEdad():#funcion
    main_zooPantalla01.locate(1,1)
    edad = input("¿Qué edad tienes?: ")
    while validaEdad(edad) == False:
        main_zooPantalla01.locate(24,1)
        print("Edad inválida.",end="")
        
        main_zooPantalla01.locate(1,1)
        edad = input("¿Qué edad tienes?: ")
    
    return int(edad)
    main_zooPantalla01.clearLine()
def printScreen():#funcion
    main_zooPantalla01.locate(5,5)
    print("Bebé....:   -")
    main_zooPantalla01.locate(6,5)
    print("Niñ@....:   -")
    main_zooPantalla01.locate(7,5)
    print("Adult@..:   -")
    main_zooPantalla01.locate(8,5)
    print("Jubilad@:   -")    
    main_zooPantalla01.locate(10,8)
    print("Total....:")

def main():
    #aquí empieza mi programa
    main_zooPantalla01.clear()
    printScreen()

    edad=pedirEdad()
    precioTotal = 0#cálculo datos


    while edad != 0:
        #calculamos tipo, precio y acumulado de entradas
        tipoE = tipoEntrada(edad)#obtengo tipo de entrada según edad introducida
        precioE = preciosE[tipoE]#obtengo precio de entrada según tipo de entrada
        numEntradas[tipoE]+=1 
        #mostramos en pantalla el cálculo de las 3 líneas superiores
        main_zooPantalla01.locate(entradasQ[tipoE]["cantidad"][0],entradasQ[tipoE]["cantidad"][1])
        print(numEntradas[tipoE])
        main_zooPantalla01.locate(entradasQ[tipoE]["precioA"][0],entradasQ[tipoE]["precioA"][1])
        print("{:7.2f}€".format(numEntradas[tipoE]*precioE))
      
        precioTotal += precioE
        main_zooPantalla01.locate(10,19)
        print("{:7.2f}€".format(precioTotal))
        edad=pedirEdad()

    main_zooPantalla01.locate(12,1)
#aquí llamo a la función que maneja mi programa
main()
