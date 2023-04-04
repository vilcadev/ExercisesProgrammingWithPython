
# 1era Forma hecha por mi
listaA=["[","{","("]
listaC=["]","}",")"]
def foundExpression(expre):   
    for i in range(len(listaA)):
        if(expre==listaA[i]):
            return listaA[i]
        elif(expre==listaC[i]):
            return listaC[i]
        else:
            continue
    return "x "
def expresionesEqui(expre):
    lista=[] 
    corcheCAcum=0
    corcheAAcum=0
    llaveCAcum=0
    llaveAAcum=0
    parenCAcum=0
    parenAAcum=0  
    boolexpresion=True
    for i in range(len(expre)):
        lista+=expre[i:i+1]    
    for x in range(len(lista)):
        if(lista[x]=="["):
            corcheAAcum+=1
        elif(lista[x]=="]"):
            corcheCAcum+=1
        elif(lista[x]=="{"):
            llaveAAcum+=1
        elif(lista[x]=="}"):
            llaveCAcum+=1
        elif(lista[x]=="("):
            parenAAcum+=1
        elif(lista[x]==")"):
            parenCAcum+=1
        else:
            #Nada, es un número
            continue    
    if(corcheAAcum==corcheCAcum):
        bandera1=True
    else:
        bandera1=False
    
    if(llaveAAcum==llaveCAcum):
        bandera2=True
    else:
        bandera2=False
    
    if(parenAAcum==parenCAcum):
        bandera3=True
    else:
        bandera3=False

    if(bandera1==True and bandera2==True and bandera3==True):
        return "La expresion: " + str(expre) + " es equilibrada: " + str(boolexpresion) 
    else:
        return "La expresion: " + str(expre) + "no es equilibrada" + str(not boolexpresion)
# Desarrollo hecho al 80%, no reconoce bien el print 5 
print(expresionesEqui("{a + b [c] * (2x2)}}}}"))    
print(expresionesEqui("{ [ a * ( c + d ) ] - 5 }"))   
print(expresionesEqui("{ a * ( c + d ) ] - 5 }"))  
print(expresionesEqui("{a^4 + (((ax4)}"))  
print(expresionesEqui("{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }"))  
print(expresionesEqui("{{{{{{(}}}}}}"))
print(expresionesEqui("(a"))

# 2da forma Mouredev, no terminada

def isBalanced(expre):
    dic_symbols={"{":"}","[":"]","(":")"}
    stack=[]
    lista=[]   
    for x in range(len(expre)):
        lista+=expre[x:x+1]
                      
    for i in range(len(lista)):
        for key,value in dic_symbols.items():
            containsKey=lista[i] in key
            containsValue= lista[i] in value       
        if(containsKey or containsValue):
            if(containsKey):
                stack.append(lista[i])
            elif(lista  or lista[i] != dic_symbols[stack.pop()]):
                return False
                       
    return lista


print(isBalanced("{a + b [c] * (2x2)}}}}")) #False    
print(isBalanced("{ [ a * ( c + d ) ] - 5 }")) #True
print(isBalanced("{ a * ( c + d ) ] - 5 }")) #False 
print(isBalanced("{a^4 + (((ax4)}")) #False
print(isBalanced("{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }")) #False 
print(isBalanced("{{{{{{(}}}}}}"))#False
print(isBalanced("(a")) #False


# 3era forma para mi la mejor

# Python3 code to Check for 
# balanced parentheses in an expression
open_list = ["[","{","("]
close_list = ["]","}",")"]

# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return i
    if len(stack) == 0:
        return "True"
    else:
        return "False"


print(check("{a + b [c] * (2x2)}}}}")) #False    
print(check("{ [ a * ( c + d ) ] - 5 }")) #True
print(check("{ a * ( c + d ) ] - 5 }")) #False 
print(check("{a^4 + (((ax4)}")) #False
print(check("{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }")) #False 
print(check("{{{{{{(}}}}}}"))#False
print(check("([{]})")) #False       

