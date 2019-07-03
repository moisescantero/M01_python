"""programa que intenta adivinar la edad del usuario usando bucle elif"""
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

if mes==1:
    transcurridos=dia
elif mes==2:
    transcurridos=31+dia
elif mes==3:
    transcurridos=31+28+dia
elif mes==4:
    transcurridos=31+28+31+dia
elif mes==5:
    transcurridos=31+28+31+30+dia
elif mes==6:
    transcurridos=31+28+31+30+31+dia
elif mes==7:
    transcurridos=31+28+31+30+31+30+dia
elif mes==8:
    transcurridos=31+28+31+30+31+30+31+dia
elif mes==9:
    transcurridos=31+28+31+30+31+30+31+31+dia
elif mes==10:
    transcurridos=31+28+31+30+31+30+31+31+30+dia
elif mes==11:
    transcurridos=31+28+31+30+31+30+31+31+30+31+dia
else:    
    transcurridos=31+28+31+30+31+30+31+31+30+31+30+dia

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
    soluciones posibles:
    -el programa responda ambos años (1987 y 1988)
    -el programa en funcion de la fgecha de hoy responda ambos
        años y la probabilidad de haber nacido en cada uno de ellos
    -el programa pregunte si ya hemos cumplido y nos diga el
        año correcto
    -el programa te pide tu fecha de nacimiento y te devuelve tu
        edad a partir de la fecha actual.
    
ESCOGEMOS LA 2a SOLUCIÓN"""