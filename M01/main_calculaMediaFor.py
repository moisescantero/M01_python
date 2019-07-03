"""creamos programa para calcular la media de una lista de
contenidos usando bucle for"""


contador=0
notas=(2,4,6,8)

def contenido(lista,indice):#función control contenido y si existe contenido
    try:    
        resultado=lista[indice]
    except:
        resultado=None#con None python dice si variable está vacía
    
    return resultado

def longitud(lista):
    indice=0
    while contenido(lista,indice)!=None:
        indice=indice+1
    
    return indice

#calcular la media
suma=0
for indice in range(0,longitud(notas)):
    suma=suma+notas[indice]

media=suma/longitud(notas)

#mostramos resultados
print("Número de items: ", longitud(notas))
print("Nota total: ",suma)
print("Nota media: ",media)