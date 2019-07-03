"""cálculo del total de una factura usando for y listas"""
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
cadenaUnidades=input("Cantidad: ")
unidades=float(cadenaUnidades)

cadenaPrecio=input("Precio unitario (€): ")
precio=float(cadenaPrecio)

totalItems=0
precioTotal=0
listaPrecios=[]
listaUnidades=[]

while unidades>0 and precio>0:
    totalUnitario=unidades*precio
    listaPrecios.append(precio)
    listaUnidades.append(unidades)
    #lineasImpresion+= "{}€ * {} unidades = {}€\n".format(precio,unidades,totalUnitario)
    totalItems+=unidades#totalItems=totalItems+unidades
    precioTotal+=totalUnitario#precioTotal=precioTotal+precio
    
    cadenaUnidades=input("Cantidad: ")
    unidades=float(cadenaUnidades)
    cadenaPrecio=input("Precio unitario (€): ")
    precio=float(cadenaPrecio)

for precio,unidades in zip(listaPrecios,listaUnidades):#empaquetamos usando función zip
    print(precio,"€ *",unidades,"unidades =",precio*unidades,"€")


print("---------------------------------------")
print("Total: ",precioTotal)
print("Unidades: ",totalItems)
