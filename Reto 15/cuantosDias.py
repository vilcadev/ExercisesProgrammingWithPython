

# Mi propuesta resuelve el problema al 100%, GG ...!
from datetime import datetime
def cuantosDias(str1,str2):
    lista1=[]
    lista2=[]
    try:
        for i in str1:
            if(datetime.strptime(str1,"%d/%m/%Y")):
               if(i!="/"):
                  lista1+=i
        for x in str2:
            if(datetime.strptime(str2,"%d/%m/%Y")):
                if(x!="/"):
                    lista2+=x
        lista1=lista1[0]+lista1[1]
        lista2=lista2[0]+lista2[1] 

        dias=int(lista1)-int(lista2)
        return abs(dias)   
    except:
        return "Error en el formato"

x=cuantosDias("12/11/2022", "29/04/2022")
print(x)

    
    