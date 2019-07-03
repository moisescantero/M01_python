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
e imprimo el resultado total en negrita, para acabar ordeno
el programa"""

"""Ahora empezamos a crear ficheros para guardar nuestros datos
al final de día, nºentradas,precios,etc"""

import main_screen01#módulo control de pantalla
import main_zooPresentacion#módulo de presentación en pantalla
from main_zooConfig import preciosE, entradasQ #módulo configuración de diccionarios
from colorama import init#módulo para mostrar caracteres ANSI en cmd
init()

numEntradas = {"Bebé":0,"Niñ@":0,"Adult@":0,"Jubilad@":0,}#diccionario para calcular datos

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

def main():
    #aquí empieza mi programa
    main_zooPresentacion.printScreen()
    edad=main_zooPresentacion.pedirEdad()
    precioTotal = 0#cálculo datos

    while edad != 0:
        #calculamos tipo, precio y acumulado de entradas
        tipoE = tipoEntrada(edad)#obtengo tipo de entrada según edad introducida
        precioE = preciosE[tipoE]#obtengo precio de entrada según tipo de entrada
        numEntradas[tipoE]+=1 
        #mostramos en pantalla el cálculo de las 3 líneas superiores
        main_screen01.Print(numEntradas[tipoE],\
                            line=entradasQ[tipoE]["cantidad"][0],\
                            column=entradasQ[tipoE]["cantidad"][1])
        main_screen01.Print("{:7.2f}€".format(numEntradas[tipoE]*precioE),\
                            line=entradasQ[tipoE]["precioA"][0],\
                            column=entradasQ[tipoE]["precioA"][1])
      
        precioTotal += precioE
        main_screen01.Print("{:7.2f}€".format(precioTotal),\
                            line=10,column=19,\
                            style='bold')
        edad=main_zooPresentacion.pedirEdad()

    main_screen01.locate(12,1)
#aquí llamo a la función que maneja mi programa
main()


