'''
numero = int(input("ingrese el numero deseado: "))

i = 1
while i <= 10:
    print(numero,"x",i,"=",numero*i)
    i += 1
'''    
    
'''    
numero = int(input("ingresa tu edad: "))

i = 1
while i <= numero:
    print("has cumplido",i,"años")
    i += 1
'''
'''
lista = ["uno", "dos", "tres"]



for i in lista:
    print(i)
    
for j in range(0,3):
    print(lista[j])
'''

'''
for i in range(1,11):
    print(i)
    
a,b = map(int,input("por favor ingrese el rango de numeros: ").split(" "))

print("--------------------------")

for j in range(a,b+1):
    print(j)    
'''  

c,d = map(int,input("por favor ingrese el rango de numeros: ").split(" "))

for i in range(c,d):
    if i%2 != 0:
        print(i)





    
        