"""creamos programa para calcular la media de una lista de
contenidos usando bucle while con la función len para ser más
rápido y eficiente"""


notas=(2,4,6,8)

#calcular la media
indice=0
suma=0
while indice <len(notas):
    suma=suma+notas[indice]
    indice=indice+1
    
media=suma/indice

#mostramos resultados
print("Número de items: ", indice)
print("Nota total: ",suma)
print("Nota media: ",media)