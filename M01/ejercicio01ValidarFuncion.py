"""creamos función para validar"""

def validacion(mensaje):
    #entrada de datos
    while True:
        try:
            strNum=int(input(mensaje))#pedimos al usuario el primer número
            break
        except ValueError:
            print("No ha introducido un número entero, vuelva a intentarlo.")
    return strNum

strNum1=validacion("Introduzca un número: ")
strNum2=validacion("Introduzca otro número: ")

#tratamiento de datos
num1=float(strNum1)
num2=float(strNum2)
diezNum1=round(num1/10,2)
diezNum2=round(num2/10,2)
suma=round(diezNum1+diezNum2,2)#usamos round("",2) para redondear a 2 decimales
resta=round(diezNum1-diezNum2,2)
mult=round(diezNum1*diezNum2,2)
div=round(diezNum1/diezNum2,2)

#salida de datos
print("El número",strNum1,"dividido entre 10 es: ",diezNum1)
print("El número",strNum2,"dividido entre 10 es: ",diezNum2)
print("La suma de",strNum1,"y",strNum2,"es: ",suma)
print("La resta de",strNum1,"y",strNum2,"es: ",resta)
print("La multiplicación de",strNum1,"y",strNum2,"es: ",mult)
print("La división de",strNum1,"y",strNum2,"es: ",div)