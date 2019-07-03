"""programa de un zoo que pide edad para calcular el
precio total de todas ellas cuando metamos un "0" para
salir validando que la edad solo sean enteros positivos,
además tenemos un módulo creado por mí para posicionar
el cursor y mejorar la presentación en pantalla,
calculo tipo de entrada según edad, saco precio según
tipo de entrada, he creado una pequeña interfaz gráfica
para presentar los datos calculados y que se actualizan
en tiempo real, ahora limpiamos la línea superior
de introducir cada uno de los valores, también le damos
formato negrita y otros estilos al texto que presento,
reseteamos el estilo para que no quede en toda la pantalla
e imprimo el resultado total en negrita"""
import main_screen
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
    edad = main_screen.Input("¿Qué edad tienes?: ",1,1)
    while validaEdad(edad) == False:
        main_screen.Format(0,33,41)
        main_screen.Print("Edad inválida",24,1,True)
        main_screen.Reset()
        edad = main_screen.Input("¿Qué edad tienes?: ",1,1)
    
    main_screen.clearLine(24)
           
    return int(edad)
    
def printScreen():#funcion
    main_screen.clear()
    main_screen.Print("Bebé....:   -",5,5)
    main_screen.Print("Niñ@....:   -",6,5)
    main_screen.Print("Adult@..:   -",7,5)
    main_screen.Print("Jubilad@:   -",8,5)
    
    main_screen.Format(1)
    main_screen.Print("Total...:   -",10,8)
    main_screen.Reset()

def main():
    #aquí empieza mi programa
    printScreen()
    edad=pedirEdad()
    precioTotal = 0#cálculo datos

    while edad != 0:
        #calculamos tipo, precio y acumulado de entradas
        tipoE = tipoEntrada(edad)#obtengo tipo de entrada según edad introducida
        precioE = preciosE[tipoE]#obtengo precio de entrada según tipo de entrada
        numEntradas[tipoE]+=1 
        #mostramos en pantalla el cálculo de las 3 líneas superiores
        main_screen.Print(numEntradas[tipoE], entradasQ[tipoE]["cantidad"][0], entradasQ[tipoE]["cantidad"][1])
        main_screen.Print("{:7.2f}€".format(numEntradas[tipoE]*precioE), entradasQ[tipoE]["precioA"][0], entradasQ[tipoE]["precioA"][1])
      
        precioTotal += precioE
        main_screen.Format(1)
        main_screen.Print("{:7.2f}€".format(precioTotal),10,19)
        main_screen.Reset()
        edad=pedirEdad()

    main_screen.locate(12,1)
#aquí llamo a la función que maneja mi programa
main()
