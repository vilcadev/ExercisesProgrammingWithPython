
# Mi propuesta resuelve el problema al 100%, GG ...!
# Recordatorio: En este problema no esta permitido usar funciones
# propias de python, como por ejemplo pasar a mayuscula
import string
# Funcion para obtener el abecedario en mayuscula( me dio flojera escribirlo)
def listAlphabet():
    return list(string.ascii_uppercase)
listaMay=listAlphabet()
print(listaMay)

listaMin=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def enMayuscula(str):
    listastr= str.split()
    l2=[]
    for i in listastr:
        if(i[0] in listaMin):
            pos=listaMin.index(i[0]) # Devuelve el indice de la coincidencia
            var=listaMay[pos]           
            i=var + i[1:] # Reemplazamos el primer caracter del string con var
            l2.append(i)  # Se agrega la palabra modificada a l2       
        else:
            l2.append(i)  
    # Convirtiendo la lista a str 
    str=" ".join(l2)   
    return str
    
print(enMayuscula("Hi everyone"))

# Forma simple, usando funciones de python
def toMayus(text):
    return text.title()
print(toMayus("hola mundo"))
        

