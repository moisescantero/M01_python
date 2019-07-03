"""programa de un zoo que pide edad para calcular el
precio total de todas ellas cuando metamos un "0" para
salir validando que la edad solo sean enteros positivos"""

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
    edad = input("¿Qué edad tienes?: ")
    while validaEdad(edad) == False:
        print("Edad inválida.")
        edad = input("¿Qué edad tienes?: ")
    
    return int(edad)


edad=pedirEdad()
precioTotal = 0

while edad != 0:
    precioE = calcularPrecioEntrada(edad)
    print("Precio Entrada: {}".format(precioE))
    precioTotal += precioE    
    edad=pedirEdad()

print("Total: {}".format(precioTotal))