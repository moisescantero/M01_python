"""importamos modulo para dibujar recorrido de una tortuga"""
import turtle 

def cuadrado(lado):#creamos función que realiza un cuadrado
    miT.forward(50) 
    miT.left(90) 
    miT.forward(50) 
    miT.left(90)
    miT.forward(50) 
    miT.left(90)
    miT.forward(50) 
    miT.left(90)
    
    return lado*lado

miT=turtle.Turtle()

area01=cuadrado(25)
miT.left(90)


area02=cuadrado(50)
miT.left(90)


area03=cuadrado(75)
miT.left(90)


area04=cuadrado(100)
miT.left(90)

