
#dic_morse={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.'}
dic_morse= {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", 
    "g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", "l": ".-..", 
    "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".__.", "q": "--.-",
    "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--.."}

def verif(word):
    bandera=False # si es false es text
    if(word.startswith(".") or word.startswith("-")):
        bandera=True # Es Morse
    else:
        bandera=False # Es Text
    return bandera

def codMorse2(text):
    acum=""
    acum2=""
    validacion=verif(text)

    if(validacion==False):
        for i in range(len(text)):
            for key,value in dic_morse.items():
                var=text[i:i+1]
                if(var==key):
                    acum+=value
            
        return "soy text :)"+acum
    else:        
        var2=text.split(" ")
        for x in range(len(var2)):           
            for key,value in dic_morse.items():  
                if(var2[x]==value):
                    acum2+=key
                    
        return "soy morse :)"+acum2           
        
            
                
        
    
    

        
 #def codMorse(palabra):
  #  acum=""
   # acum2=""
    #for i in range(len(palabra)):  
     #for key,value in dic_morse.items():
      #  var=palabra[i:i+1]
       # var2=palabra.split(" ")
        #if(var==key):
         #   acum+=value       
        #elif(var2[0]==value):
         #   acum2+=key
    #return acum

texto="chocapic. es una marca de cereales"
print(codMorse2(texto))
print("se ejecuto")
