
import math

def decimalABinario(dec):
    var=dec
    acum=""
    while(var!=0):
        if(var%2==0):
            acum+="0"
        elif(var%2==1):
            acum+="1"      
        var=math.trunc(var/2)
    return acum[::-1]
print(decimalABinario(28))


