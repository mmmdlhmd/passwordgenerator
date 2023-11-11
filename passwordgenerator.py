
#Password Generator yazmak input alicak length azel karakter olup olmadigini alicak ona gore password generate edicek
#>>> Please enter the length of the password: 16
#>>> Is Alpha-numeric supported: y/n         
#>>> Is Special character supported: y/n     (*,.][}{@$#%^)
#>>> Generated password is: sa445ssff[+/
import re
import string
import random

p=[]
k=[]

spe=(string.punctuation)
spe=list(spe)

r=(0,1,2,3,4,5,6,7,8,9)
r=list(r)
lowup=list(string.ascii_lowercase)+list(string.ascii_uppercase)
thel = lowup+list(r)
thel=list(thel)

n=int(input("Please enter the length of the password: "))

an=input("Is Alpha-numeric supported: (y/n)   ")
sc=input("Is Special character supported: (y/n)   ")

def listToString(p):
    str1 = ""
    for i in p:
        str1 +=str(i)
    return str1
def contains_number():
    return any(char.isdigit() for char in listToString(p))
def contains_letter():
    return any(char.isalpha() for char in listToString(p))
def contains_spe():
    return any(char in spe for char in listToString(p))


if (an=="y" or an=="Y") and (sc=="n" or sc=="N"):
    k=thel
    for i in range(0,n):
        p.append(random.choice(k))
    while True:
        if contains_number() and contains_letter():
            print(listToString(p))
            break


elif (an=="y" or an=="Y") and (sc=="y" or sc=="Y"):
    k=thel+spe
    for i in range(0,n):
        p.append(random.choice(k))
    while True:
        if contains_number() and contains_letter() and contains_spe():
            print(listToString(p))
            break
    
elif (an=="n" or an=="N") and (sc=="y" or sc=="Y"):
    k=spe
    for i in range(0,n):
        p.append(random.choice(k))
    while True:
        if contains_spe():
            print(listToString(p))
            break


elif (an=="n" or an=="N") and (sc=="n" or sc=="N"):
    print("Please try again")
else:
    print("Please try again")








#print(p)

#print(contains_spe)
#print(contains_letter())




    
                    
                          
                
                
                            
                                       

                        