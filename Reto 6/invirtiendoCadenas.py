# 1 era Forma
mistring="Hola Mundo"
stringaux=""

# Recuerda: 
# Lo de [::-1] es un "truco" frecuentemente usado en python para obtener
# una lista o una cadena "del revés". Se basa en el operador slice (rodaja) cuya sintaxis general es:

# iterable[inicio:fin:paso]
# que permite extraer una serie de elementos del iterable,
# comenzando por el numerado como inicio y terminando por el numerado como fin-1, aumentando de paso en paso.

# Si omites inicio se empezará en el primer elemento del iterable, 
# si omites fin se terminará en el último elemento del iterable.

# Si el paso es negativo, el iterable se recorre "hacia atrás", 
# y en ese caso los valores por defecto cuando se omite inicio y fin se invierten.

# Así pues iterable[::-1] devuelve los elementos del iterable, 
# comenzando por el último y terminando por el primero, en orden inverso a como estaban.

stringaux = mistring[::-1]
   
print(stringaux)

# 2da Forma (con bucle for):

# Creamos una funcion

def reverse(mistring):
    mistringlen=len(mistring)-1 # Asignamos el tamaño
    reversedtext=""
    for i in range(mistringlen+1):
        reversedtext+=mistring[mistringlen-i] # Recorremos desde el ultimo elemento al primero
                                                # Asi se ira almacenando uno a uno en el nuevo string

    return reversedtext # Devolvemos la cadena
print(reverse(mistring))

# 3era Forma (recursividad):

# Recibe 3 parametros: el texto, el indice empezara en 0, y el texto en reversa que inicialmente estara vacío
def recursiveReverse(mistring,index=0,reversedText=""):
    textCount = len(mistring)-1
    newReversedText=reversedText # Asigno la letra
    newReversedText+=mistring[textCount-index] # Se va añadiendo la otra letra de la posición
    
    if(index<textCount):
        newIndex=index+1 # Incrementa el indice
        newReversedText=recursiveReverse(mistring,newIndex,newReversedText) # Recursividad
    return newReversedText

print(recursiveReverse(mistring))