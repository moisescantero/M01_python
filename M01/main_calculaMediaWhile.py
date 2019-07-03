"""creamos programa para calcular la media de una lista de
contenidos usando bucle while"""


contador=0
notas=(2,4,6,8)

def contenido(lista,indice):#función control contenido y si existe contenido
    try:    
        resultado=lista[indice]
    except:
        resultado=None#con None python dice si variable está vacía
    
    return resultado


#sumar notas
indice=0
suma=0
while contenido(notas,indice):
    suma=suma+notas[indice]
    indice=indice+1
    
#calculamos media
media=suma/indice

#mostramos resultados
print("Número de items: ", indice)
print("Nota total: ",suma)
print("Nota media: ",media)