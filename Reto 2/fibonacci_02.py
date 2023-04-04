
# Escribe un programa que imprima por consola los n números de la sucesión de Fibonacci empezando en 0, Haciendo uso de la recursividad.
#  - La serie Fibonacci se compone por una sucesión de números en
#    la que el siguiente siempre es la suma de los dos anteriores.
#    0,1,1,2,3,5,8,13
# Problema dificíl si o hacer eres god literalmente


def fibonacci(n):
    if(n==0):
        return n 
    elif(n==1):
        return n   
    else:
        return fibonacci(n-1) + fibonacci(n-2)

x=input("Ingresa el n\n")
x=(int(x))
for i in range(0,x+1):  
    print(fibonacci(i))





        
     



def fibomejor():
     n0=0
     n1=1

     for i in range(1,6):
        print(n0)

        fib=n0+n1
        n0=n1
        n1=fib

#abajo
fibomejor()






        


         