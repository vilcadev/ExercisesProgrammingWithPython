
# Mi propuesta resuelve el problema al 100%, GG ...!
import math
def esNumeroAmstrong(num):
    lista=[]
    text=str(num)
    acum=0
    if(num<0):
        return False
    for i in text:
        lista+=list(i)   
    for x in range(len(lista)):
        acum+=math.pow(int(lista[x]),len(lista))   
    if(num==int(acum)):
        return True
    else:
        return False
print(esNumeroAmstrong(154))
#DANIEL SIN POTO