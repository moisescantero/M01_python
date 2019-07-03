"""programa que intenta adivinar la edad del usuario"""
nombre=input("¿Cómo te llamas? ")#guardamos entrada teclado en variable n
print("Hola,",nombre)#imprimimos entrada de teclado guardada en variable n
strAño=input("Introduce año actual ")#guardamos año actual
strEdad=input("Introduce tu edad ")#guardamos edad
año=int(strAño)#asignamos valor entero de cadena texto y asginamos a variable
edad=int(strEdad)#asignamos valor entero de cadena texto y asignamos a variable
nacimiento = año - edad#error de operandos porque estamos restando dos cadenas de texto
print(nombre, "naciste en ", nacimiento)
"""ES IMPORTANTE QUE LA INTRODUCCIÓN ERRÓNEA DE DATOS POR PARTE
DEL USUARIO SE DEBE GESTIONAR DE MANERA EFICIENTE"""
