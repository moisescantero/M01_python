"""vamos a contar cada caracter de una cadena usando
diccionarios."""

miTexto=("Tres palabras para ti.")

frecuencias=dict()#creamos diccionario vacío
#relleno y compruebo cada una de las posiciones de la cadena hasta acabar.
for caracter in miTexto:
    if caracter in frecuencias:#comprobamos posicion y modificamos valor si ya existe
        frecuencias[caracter]+=1
    else:#o asignamos valor si es la primera vez que aparece el caracter
        frecuencias[caracter]=1
#imprimo los valores para cada clave valor.
for caracter in frecuencias.keys():
    print(caracter, "-", frecuencias[caracter])