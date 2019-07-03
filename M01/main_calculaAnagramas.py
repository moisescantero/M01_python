"""programa que identifique si dos palabras son anagra-
mas. amor y roma por ejemplo."""

def isAnagramaSimple(p1,p2):
    
    listaComparacionLetras=[]
    if len(p1)!=len(p2):
        return False
    
    for caracter1 in p1:
        haPasadoPorAqui=False
        for caracter2 in p2:
            if caracter1 == caracter2:
                haPasadoPorAqui=True
                listaComparacionLetras.append(True)
        if not haPasadoPorAqui:
            listaComparacionLetras.append(False)
    
    if False in listaComparacionLetras:
        return False
    else:
        return True

def isAnagrama(p1,p2):
    return isAnagramaEle(p1,p2) and isAnagramaEle(p2,p1)

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

def isAnagramaDic(p1,p2):
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

print(__name__)
