import main_calculaAnagramas#modulo hecho por mí

p1=input("Una palabra: ")
p2=input("Otra palabra: ")

if main_calculaAnagramas.isAnagramaDic(p1,p2):
    print(p1," y ",p2," son anagramas.")
else:
    print(p1," y ",p2," NO son anagramas.")

