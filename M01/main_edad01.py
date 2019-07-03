"""programa que intenta adivinar la edad del usuario"""

nombre=input("¿Cómo te llamas? ")#guardamos entrada teclado en variable n
print("Hola,",nombre)#imprimimos entrada de teclado guardada en variable n
strAño=input("Introduce año actual ")#guardamos año actual
strEdad=input("Introduce tu edad ")#guardamos edad
strCumplidos=input("¿Cumplista años ya? ")

año=int(strAño)#asignamos valor entero de cadena texto y asginamos a variable
edad=int(strEdad)#asignamos valor entero de cadena texto y asignamos a variable

if strCumplidos=="s":
    nacimiento = año - edad#error de operandos porque estamos restando dos cadenas de texto
else:    
    nacimiento = año - edad-1#error de operandos porque estamos restando dos cadenas de texto

print(nombre, "naciste en ", nacimiento)
"""ES IMPORTANTE QUE LA INTRODUCCIÓN ERRÓNEA DE DATOS POR PARTE
DEL USUARIO SE DEBE GESTIONAR DE MANERA EFICIENTE"""
"""errores que vamos a resolver en este archivo:
    -tratamiento de tipo de datos incorrecto de entrada
    -error en el cálculo del año de nacimiento si aún no se
        han cumplido los años.
    -trabajar con la fecha del sistema
    soluciones posibles:
    -el programa responda ambos años (1987 y 1988)
    -el programa en funcion de la fgecha de hoy responda ambos
        años y la probabilidad de haber nacido en cada uno de ellos
    -el programa pregunte si ya hemos cumplido y nos diga el
        año correcto
    -el programa te pide tu fecha de nacimiento y te devuelve tu
        edad a partir de la fecha actual.
    
ESCOGEMOS LA 2a SOLUCIÓN"""