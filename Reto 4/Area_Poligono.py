import math
def areaPoligono(eleccion,base,altura):
    if(eleccion=="1"):
        return (base*altura)/2
    elif(eleccion=="2"):
         return math.pow(altura,2)
    elif(eleccion=="3"):
         return base*altura 

#Puedes mejorar el menu con un while y un regreso al menu
print("***Menu***")
print("[1] Calcular Area Triangulo")
print("[2] Calcular Area Cuadrado")
print("[3] Calcular Area Rectangulo")
print("[4] Exit")



var=input()
if(var=="1"):
    print("Ingrese la base")
    base=int(input())
    print("Ingrese la altura")
    altura=int(input())
    print("Area Triangulo es: "+ str(areaPoligono(var,base,altura)))
elif(var=="2"):
    base=0    
    print("Ingrese la altura")
    altura=int(input())
    print("Area Cuadrado es: "+ str(areaPoligono(var,base,altura)))
elif(var=="3"):
    print("Ingrese la base")
    base=int(input())
    print("Ingrese la altura")
    altura=int(input())
    print("Area rectangulo es: "+str(areaPoligono(var,base,altura)))
else:
    print("Hasta pronto")  




       



   



