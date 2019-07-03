"""programa que intenta adivinar la edad del usuario usando listas y tuplas"""
"""mes01=31
mes02=28
mes03=31
mes04=30
mes05=31
mes06=30
mes07=31
mes08=31
mes09=30
mes10=31
mes11=30
mes12=31"""

strnombre=input("¿Cómo te llamas? ")#guardamos entrada teclado en variable n
print("Hola,",strnombre)#imprimimos entrada de teclado guardada en variable n

strAño=input("Introduce año actual ")#pedimos al usuario año actual
strMes=input("En que mes estamos ")#pedimos al usuario mes actual
strDia=input("En que dia estamos ")#pedimos al usuario dia actual
strEdad=input("Introduce tu edad ")#pedimos edad al usuario

año=int(strAño)#valor entero de cadena de texto guardado en variable
mes=int(strMes)#valor entero de cadena de texto guardado en variable
dia=int(strDia)#valor entero de cadena de texto guardado en variable
edad=int(strEdad)#valor entero de cadena de texto guardado en variable

#tuplaMeses=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")#la tupla es inmutable(no se pueden cambiar los valores internos
#diasMes=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]#la lista se puede mutar (cambiar valores internos)
diasMes=(31,28,31,30,31,30,31,31,30,31,30,31)#tupla que contiene los días de cada mes del año
transcurridos=0
indice=0
while indice<mes-1:
    transcurridos=transcurridos+diasMes[indice]
    indice=indice+1


transcurridos=transcurridos+dia
prob=transcurridos/365*100
nacimiento = año - edad

print(nombre, "naciste en", nacimiento, "con una probabilidad de",prob)
print("o en", nacimiento-1, "con una probabilidad de",100-prob)


"""ES IMPORTANTE QUE LA INTRODUCCIÓN ERRÓNEA DE DATOS POR PARTE
DEL USUARIO SE DEBE GESTIONAR DE MANERA EFICIENTE"""
"""errores que vamos a resolver en este archivo:
    -tratamiento de tipo de datos incorrecto de entrada
    -error en el cálculo del año de nacimiento si aún no se
        han cumplido los años.
    -trabajar con la fecha del sistema
    -que pasa con los bisiestos
    -formatear salida para dos decimales

    soluciones posibles:
    -el programa responda ambos años (1987 y 1988)
    -el programa en funcion de la fgecha de hoy responda ambos
        años y la probabilidad de haber nacido en cada uno de ellos
    -el programa pregunte si ya hemos cumplido y nos diga el
        año correcto
    -el programa te pide tu fecha de nacimiento y te devuelve tu
        edad a partir de la fecha actual.

    
ESCOGEMOS LA 2a SOLUCIÓN"""