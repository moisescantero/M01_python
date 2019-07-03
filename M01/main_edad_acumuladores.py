"""programa que intenta adivinar la edad del usuario usando acumuladores"""
mes01=31
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
mes12=31
transcurridos=0
nombre=input("¿Cómo te llamas? ")#guardamos entrada teclado en variable n
print("Hola,",nombre)#imprimimos entrada de teclado guardada en variable n

strAño=input("Introduce año actual ")#pedimos al usuario año actual
strMes=input("En que mes estamos ")#pedimos al usuario mes actual
strDia=input("En que dia estamos ")#pedimos al usuario dia actual
strEdad=input("Introduce tu edad ")#pedimos edad al usuario

año=int(strAño)#valor entero de cadena de texto guardado en variable
mes=int(strMes)#valor entero de cadena de texto guardado en variable
dia=int(strDia)#valor entero de cadena de texto guardado en variable
edad=int(strEdad)#valor entero de cadena de texto guardado en variable

if mes>1:#bucle if usando varibale transcurridos como un acumulador de valores
    transcurridos=transcurridos+mes01
if mes>2:
    transcurridos=transcurridos+mes02
if mes>3:
    transcurridos=transcurridos+mes03
if mes>4:
    transcurridos=transcurridos+mes04
if mes>5:
    transcurridos=transcurridos+mes05
if mes>6:
    transcurridos=transcurridos+mes06
if mes>7:
    transcurridos=transcurridos+mes07
if mes>8:
    transcurridos=transcurridos+mes08
if mes>9:
    transcurridos=transcurridos+mes09
if mes>10:
    transcurridos=transcurridos+mes10
if mes>11:
    transcurridos=transcurridos+mes11#hasta aquí bucle if con acumulador

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