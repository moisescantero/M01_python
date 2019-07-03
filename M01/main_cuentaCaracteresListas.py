"""vamos a contar cada caracter de una cadena usando
listas."""
"""en lista si a=b(reetiquetamos) y modificamos se
cambian ambas listas, para que eso no pase usamos
c=a[:](clonamos), creamos una nueva lista que no
resultará modificada cuando lo hagamos con la lista a"""

def existe(letra, lista):
    posicion=0
    while posicion< len(lista):
        if lista[posicion]==letra:
            return posicion
        posicion+=1
    return None#valor vacío o no he encontrado nada

miTexto=("tres palabras para ti.")
letras=[]
frecuencias=[]

for caracter in miTexto:
    posicion= existe(caracter, letras)#funcion que nos da la posicion en la cadena
    if posicion!= None:#si existe caracter incrementamos en 1
        frecuencias[posicion]+= 1
    else:
        letras.append(caracter)
        frecuencias.append(1)

indice=0
while indice<len(letras):
    print(letras[indice], "-", frecuencias[indice])
    indice+=1