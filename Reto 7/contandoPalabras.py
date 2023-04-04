# 1era forma del reto:
# Los caracteres que no contamos como palabras
texto="adios mundo cruel adios adios"
quitar= ",;:.\n!\"'"

for caracter in quitar:
    texto = texto.replace(caracter,"") # Reemplazarlo por nada, es decir, removerlo

# Lo convertimos a minúsculas pues una palabra mayúscula y minúscula cuenta como una sola
texto = texto.lower()

# Las palabras están separadas por un espacio así que convertimos la cadena a arreglo
palabras = texto.split(" ")

# Ahora vamos a contar las palabras creando un diccionario. En este caso la clave del diccionario
# será la palabra, y el valor será el conteo
diccionario_frecuencias={}
for palabra in palabras:
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra]+=1
    else:
        diccionario_frecuencias[palabra]=1 # La primera pasada entra aca ya que el diccionario
                                           # inicialmente esta vacio

for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra] # Accedemos al valor atraves de la clave palabra
    print(f"La palabra '{palabra}'tiene una frecuencia de {frecuencia}")


# 2da forma: Algo asi seria con funciones propias de python, esta medias me fui a comer
for palabra in palabras:
    frecuencia=texto.count(palabra)
    print("si"+str(palabra)+"frecuencia:"+str(frecuencia))   

        

    

    



