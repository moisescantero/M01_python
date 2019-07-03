"""cálculo de total de una factura usando diccionario"""
"""los diccionarios no función con índice numérico sino string"""
"""se introduce precio unitario y cantidad de productos,
seguirá introduciendo ambos valores hasta que ponga 0. Este
último precio será descartado."""
"""restricciones:
    -números decimales para precio y enteros positivos para cantidad.
    -el programa advierte dato no numérico y volverá a pedirlo.
    -resultado de precio se redondea a 2 decimales.
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
_UNIDADES=0
_PRECIO=1
cadenaUnidades=input("Cantidad: ")
unidades=float(cadenaUnidades)

cadenaPrecio=input("Precio unitario (€): ")
precio=float(cadenaPrecio)

totalItems=0
precioTotal=0

listaLineasFact=[]

while unidades>0 and precio>0:
    totalUnitario=unidades*precio
    item=dict()
    item['unidades']= unidades
    item['precio']= precio
    listaLineasFact.append(item)

    #lineasImpresion+= "{}€ * {} unidades = {}€\n".format(precio,unidades,totalUnitario)
    totalItems+=unidades#totalItems=totalItems+unidades
    precioTotal+=totalUnitario#precioTotal=precioTotal+precio
    
    cadenaUnidades=input("Cantidad: ")
    unidades=float(cadenaUnidades)
    cadenaPrecio=input("Precio unitario (€): ")
    precio=float(cadenaPrecio)

for item in listaLineasFact:#empezamos a usar estructuras complejas
    print(item['precio'],"€ *",item['unidades'],"unidades =",item['unidades']*item['precio'],"€")

#tres líneas de código para imprimir resultados
print("---------------------------------------")
print("Total: ",precioTotal)
print("Unidades: ",totalItems)
#la línea de abajo es alternativa usando format para imprimir usando solo una línea de código
print("---------------------------------------\nTotal:\t{:.2f}\nUnidades:\t{:.2f}".format(precioTotal,totalItems))
#/ \n=retorno de carro/ / \t=tabulador/ /{}=reservar posicion para valor/ /:.2f=redondear a 2 decimales/
print("\033[3;33;41m")#caracteres de control para formateo de resultados