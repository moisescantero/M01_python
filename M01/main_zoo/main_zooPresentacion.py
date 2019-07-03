import main_screen01
def validaEdad(cadena):#validar que solo acepte positivos
    try:
        n = int(cadena)
        if n>= 0:#entonces el valor es válido
            return True
        return False
    except:
        return False
    
def pedirEdad():#funcion
    edad = main_screen01.Input("¿Qué edad tienes?: ",line=1,column=1)
    while validaEdad(edad) == False:
        main_screen01.Print("Edad inválida",line=24,column=1,\
                            style="bold",colors="yellow",back="red",)
        edad = main_screen01.Input("¿Qué edad tienes?: ",line=1,column=1)
    
    main_screen01.clearLine(24)
           
    return int(edad)
    
def printScreen():#funcion
    main_screen01.clear()
    main_screen01.Print("Bebé....:   -",line=5,column=5)
    main_screen01.Print("Niñ@....:   -",line=6,column=5)
    main_screen01.Print("Adult@..:   -",line=7,column=5)
    main_screen01.Print("Jubilad@:   -",line=8,column=5)
    
    main_screen01.Format(1)
    main_screen01.Print("Total...:   -",line=10,column=8)
    main_screen01.Reset()
