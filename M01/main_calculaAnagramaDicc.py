"""introducimos en shell isAnagrama(p1,p2) nos dice si
es un anagrama o no devolviendo booleanos True o False"""

def contarCaracteres(cadena):
    resultado=dict()#es un diccionario que accede por clave"""    
    for caracter in cadena:
        if caracter in resultado:
            resultado[caracter]+=1
        else:
            resultado[caracter]=1
    return resultado#variable que contiene un diccio-
#nario con todas las letras en forma de clave y todas
#sus frecuencias en forma de valor

def isAnagrama(p1,p2):
    dP1=contarCaracteres(p1)
    dP2=contarCaracteres(p2)
    if len(dP1)!=len(dP2):
        return False
    for caracter in dP1:
        if caracter in dP2 and dP1[caracter]==dP2[caracter]:
            pass
        else:
            return False
    return True