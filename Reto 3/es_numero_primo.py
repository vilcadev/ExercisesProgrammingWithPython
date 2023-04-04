import sys
# Ejercicio resuelto con pura lógica gg
for i in range(2,101):
    bandera=0
    for x in range(2,i+1):
        if(i%x==0):
            bandera+=bandera+1
    if(bandera<=1):
        sys.stdout.write("["+str(i)+"]"+" ")
    

# Otra forma de hacerlo

def esPrimo(number):
    if(number<2):
        return False  
    for y in range(2,number):
        if(number%y==0):
            return False    
    return True

print(" \nLa otra Forma: ")

for m in range(2,101):
    if(esPrimo(m)):
        sys.stdout.write("["+str(m)+"]"+" ")
print("ejecuto?: "+ "si gg")




        
        


     
        