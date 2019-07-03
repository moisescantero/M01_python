"""cálculo del total de una factura usando while, listas de
listas, estructuras complejas y constantes"""
"""se introduce precio unitario y cantidad de productos,
seguirá introduciendo ambos valores hasta que ponga 0. Este
último precio será descartado."""
"""restricciones:
    -números decimales para precio y enteros positivos para cantidad.
    -el programa advierte dato no numérico y volverá a pedirlo.
    -resultado del precio se redondea a 2 decimales.
puntos a valorar:
    -diferenciar entrada, procesamiento y salida de datos con
    comentarios o agrupando
retos:
    -crear función valoración de enteros.
    -crear módulo reutilizable con la función de valoración de
    decimales y utilizarlo en el programa
    -utilizar python format para formatear la salida impresa.
    -utilizar if para distinguir unidad/unidades en función de
    la cantidad de producto
"""
_UNIDADES=0#las constantes mejoran la legibilidad del código
_PRECIO=1

def informaItem(precio,unidades):
    item=[]
    item.append(unidades)
    item.append(precio)
    return item
    
cadenaUnidades=input("Cantidad: ")
unidades=float(cadenaUnidades)

cadenaPrecio=input("Precio unitario (€): ")
precio=float(cadenaPrecio)

totalItems=0
precioTotal=0
listaPrecios=[]
listaUnidades=[]
listaLineasFact=[]

while unidades>0 and precio>0:
    totalUnitario=unidades*precio
    item=informaItem(precio,unidades)
    listaLineasFact.append(item)

    #lineasImpresion+= "{}€ * {} unidades = {}€\n".format(precio,unidades,totalUnitario)
    totalItems+=unidades#totalItems=totalItems+unidades
    precioTotal+=totalUnitario#precioTotal=precioTotal+precio
    
    cadenaUnidades=input("Cantidad: ")
    unidades=float(cadenaUnidades)
    cadenaPrecio=input("Precio unitario (€): ")
    precio=float(cadenaPrecio)

for item in listaLineasFact:#empezamos a usar estructuras complejas
    print(item[_PRECIO],"€ *",item[_UNIDADES],"unidades =",item[_UNIDADES]*item[_PRECIO],"€")


print("---------------------------------------")
print("Total: ",precioTotal)
print("Unidades: ",totalItems)
