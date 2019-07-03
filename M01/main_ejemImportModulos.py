"""importamos módulos propios o de serie para utilizar
sus funciones internas y mejorar la funcionalidad de
nuestro programa aprovechando código externo."""
"""usando en shell dir() y help() con nombre de módulo
obtengo directorio y ayuda de las funciones dentro de
módulo"""

#import main_calculaAnagramas#modulo hecho por mí
#import math#modulo de serie en python importado entero
from math import factorial as fact#extraigo de diccionario la función concreta que me interesa"""
                                  #usando as le doy un alias
"""p1=input("Una palabra: ")
p2=input("Otra palabra: ")

if main_calculaAnagramas.isAnagramaDic(p1,p2):
    print(p1," y ",p2," son anagramas.")
else:
    print(p1," y ",p2," NO son anagramas.")"""

n=input("Número: ")
#print(math.factorial(int(n)))#para import math
#print("PI vale: {}".format(math.pi))#para import math
#print(factorial(int(n)))#para from math import factorial uso funcion concreta
print(fact(int(n)))#para from math import factorial uso funcion concreta
