"""convertir caracteres a número hexadecimal"""
digitos16=("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f",)
angulo=360/16

cadena="Hola"

for caracter in cadena:
    valorHexadec= hex(ord(caracter))
    digito1=valorHexadec[2]
    digito2=valorHexadec[3]

    print(digito1)
    print(digito2)
