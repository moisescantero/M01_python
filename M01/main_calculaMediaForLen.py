"""creamos programa para calcular la media de una lista de
contenidos usando bucle for con la función len para ser más
rápido y eficiente"""


notas=(2,4,6,8)
suma=0
longNotas=len(notas)
for indice in range(0,longNotas):
    suma=suma+notas[indice]

media=suma/longNotas

#mostramos resultados
print("Número de items: ", longNotas)
print("Nota total: ",suma)
print("Nota media: ",media)