# hola    mundo     out1= hla   out2= mund

# Desarrollo al 100% GG ...!
def deleteCaracter(str1,str2):
    lista1=[]
    lista2=[]
    for a in str1:
        lista1+=list(a)
    for b in str2:
        lista2+=list(b)   
    for x in lista1:       
        for y in lista2:
            if(x==y):
                lista1.remove(x)
                lista2.remove(y)
    stra="".join(lista1) #convertimos de lista a string
    strb="".join(lista2) #convertimos de lista a string   
    return stra,strb
l1,l2=deleteCaracter("hola","mundo")
print(l1,l2)

