"""pasar valores para funciones con argumentos variables"""

def imprimeCosas(*listaCosas):
    for item in listaCosas:
        print(item)
        
"""pasar clave=>valor para funciones con argumentos variables"""
def imprimeConDiccionario(**diccionarioParametros):
    if "line" in diccionarioParametros:
        print("Posicionar en línea ",diccionarioParametros["line"])
    else:
        print("No hay line.")

imprimeCosas("cosa 1","cosa 2","cosa 3","cosa 4")
imprimeConDiccionario(contenido="la cosa", line=3,column=5)
