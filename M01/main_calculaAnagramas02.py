"""programa que identifique si dos palabras son anagra-
mas. amor y roma por ejemplo."""

def isAnagramaEle(p1,p2):
    
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

