# Mi propuesta resuelve el problema al 100%, GG ...!
from atleta import *  #Importamos la clase atleta para el (run,jump)


def checkRace(milista,str):    
    bandera=bool
    if(len(milista)==len(str)):
        for i in range(len(milista)):
            if(milista[i]=="run"):
                if(str[i]=="_"):
                    bandera=True
                else:               
                    l=list(str)
                    l[i]="/"
                    str="".join(l)
                    bandera=False
            else:
                if(str[i]=="|"):
                    bandera=True
                else:
                
                    l=list(str)
                    l[i]="x"
                    str="".join(l)
                    bandera=False
    elif(len(milista)>len(str)):# si cumple: el atleta hizo mas acciones y debemos completar con "?"
        var=len(milista)-len(str)
        for x in range(abs(var)): #Aplicamos abs para obtener el valor absoluto y no negativos
            str+="?"
        bandera=False
    else: #Sino entonces hay mas pista que acciones del atleta, reemplazamos con "?"
        var=len(milista)-len(str)
        for y in range(abs(var)):
            l=list(str)
            l[y+len(milista)]="?"
            str="".join(l)
        bandera=False
               
    return str,bandera
obj=atleta() #Creamos un objeto de tipo atleta, para acceder a los metodos de la clase
lista=obj.jump(),obj.run(),obj.jump(),obj.jump() # Llenamos la lista con acciones
mistr,mibool=checkRace(lista,"|_||")
print(mistr,mibool)