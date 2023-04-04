
# Mi propuesta resuelve el problema al 100%, GG ...!
# Nota: para limpiar -> (NORMALIZAR) nuestro texto de ".",",", espacios,numeros , también
# podemos usar el import re, el cual nos sirve para todo este tipo de cosas
# pagina donde se habla mas sobre esta libreria:
# https://www.geeksforgeeks.org/normalizing-textual-data-with-python/

expresiones=[".",","," "]
def isPalindromo(stringtext):
    lista=[]  
    text=stringtext.lower()
    for i in text:
        if(i not in expresiones):
            lista+=list(i)
    listai=list(reversed(lista))
    if(lista==listai):
        return True
    else:
        return False  
print(isPalindromo("Ana Lleva al oso la avellana"))
