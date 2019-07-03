def myUpper(cadena):
    resultado = ""
    
    for caracter in cadena:#recorrido=cantidad de caracteres
        codigoCaracter=ord(caracter)#conversion letra a numero
        if codigoCaracter >= 97 and codigoCaracter<=122:#rango de mayusculas en la tabla ASCII
            codigoMayus= codigoCaracter-32#número menos 32
            caracterMayus=chr(codigoMayus)#conversion número a letra
            resultado= resultado + caracterMayus
        else:
            resultado=resultado+caracter
        
    return resultado

palabras=input("Dime algo bajito: ")
print("Yo te grito: ",myUpper(palabras))