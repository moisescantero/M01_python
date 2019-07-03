"""transformar caracter a UTF o ASCII"""

cadena=("Hola")#conversion de caracter a numero
for caracter in cadena:
    print(caracter, "-", ord(caracter))

#conversion de numero a caracter
car=int(input("Dame un número entre 32 y 127: "))
print(car, "-", chr(car))
