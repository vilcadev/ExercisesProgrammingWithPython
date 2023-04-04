

def isAnagram(string1,string2):
    inv="".join(reversed(string2))
    if(string1==inv):
        return True
    else:
        return False

print(isAnagram("roma","amor"))


    


