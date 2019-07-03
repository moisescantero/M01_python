"""programa que calcula el área de un triangulo"""
"""el programa debe pedir base y altura para devolver la super
ficie de triangulo area=(base*altura)/2"""
"""restricciones:
    -se admiten decimales como entrada de datos
    -solo se admiten datos numéricos y si no se sale del programa
    -redondear área de triángulo a 2 decimales
puntos a valorar:
    -diferenciar entrada, procesamiento y salida de datos con
    comentarios o agrupando
retos:
    -crear función para validar números decimales
    -crear módulo reutilizable con la función de valoración de
    decimales y utilizarlo en el programa
"""
def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False

B=input("Base del triángulo: ")
if esDecimal(B):
    b=float(B)
    
    H=input("Altura del triángulo: ")

    if esDecimal(H):
        h=float(H)
        area=b*h/2    
        print("Superficie del triángulo: ", round(area,2))

    else:
        print(H,"debe ser un número")
        
else:
    print(B,"debe ser un número")
    