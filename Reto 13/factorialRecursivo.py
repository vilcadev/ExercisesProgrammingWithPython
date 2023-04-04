
# Mi propuesta resuelve el problema al 100%, GG ...!
def factorialRecursivo(num):
    acum=0
    if(num<0):
        return 0
    elif(num<=1):
        return 1
    else:
        acum+=num*factorialRecursivo(num-1)
    return acum
print(factorialRecursivo(1))

    
    
