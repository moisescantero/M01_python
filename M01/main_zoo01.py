"""programa de un zoo que pide edad para calcular el
precio total de todas ellas cuando metamos un "0" para
salir"""

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


def pedirEdad():
    edad = input("¿Qué edad tienes?: ")
    edad = int(edad)#validar entrada
    return edad

edad=pedirEdad()
precioTotal = 0

while edad != 0:
    precioE = calcularPrecioEntrada(edad)
    print("Precio Entrada: {}".format(precioE))
    precioTotal += precioE    
    edad=pedirEdad()

print("Total: {}".format(precioTotal))