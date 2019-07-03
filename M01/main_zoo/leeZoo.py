from main_zooConfig import preciosE


fEntradas = open("transacciones.txt", "r")

numEntradasBebe=0
numEntradasNiño=0
numEntradasAdulto=0
numEntradasJubilado=0

linea = fEntradas.readline()
totalEntradas=0
totalPrecio=0

while linea != "":
    entradas = linea.split(",")
    
    numEntradasBebe += int(entradas[0])
    numEntradasNiño += int(entradas[1])
    numEntradasAdulto += int(entradas[2])
    numEntradasJubilado += int(entradas[3])
    
    totalEntradas += int(entradas[0])
    totalEntradas += int(entradas[1])
    totalEntradas += int(entradas[2])
    totalEntradas += int(entradas[3])

    linea=fEntradas.readline()

print("Entradas de Bebé....: {:3d} - {:7.2f}".format(numEntradasBebe,\
                                                     numEntradasBebe *\
                                                     preciosE["Bebé"] ))
print("Entradas de Niñ@....: {:3d} - {:7.2f}".format(numEntradasNiño,\
                                                     numEntradasNiño *\
                                                     preciosE["Niñ@"]))
print("Entradas de Adult@..: {:3d} - {:7.2f}".format(numEntradasAdulto,\
                                                     numEntradasAdulto *\
                                                     preciosE["Adult@"]))
print("Entradas de Jubilad@: {:3d} - {:7.2f}".format(numEntradasJubilado,\
                                                     numEntradasJubilado *\
                                                     preciosE["Jubilad@"]))

print("\nTotal: {:3d} - {:7.2f}€".format(totalEntradas,\
                                         numEntradasBebe *\
                                         preciosE["Bebé"] +\
                                         numEntradasNiño *\
                                         preciosE["Niñ@"]\
                                         +numEntradasAdulto *\
                                         preciosE["Adult@"] +\
                                         numEntradasJubilado *\
                                         preciosE["Jubilad@"]))