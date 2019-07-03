"""hacemos la suma de los 100 primeros números usando for
para practicar iteraciones(repeticiones)"""

sumaTotal=0

for counter in range(1,101):#hasta 101 para incluir 100 xq python
    sumaTotal=sumaTotal+counter#no incluye ultimo valor en bucle for
    counter+=counter
print("Total: ",sumaTotal)
