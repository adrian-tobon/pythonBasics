lista = [4,56,78,14,33,18]

def calculoPromedio(a,b):
    return (a+b)/2

def agregarALista():
    numero = input("ingrese el numero: ")
    lista.append(int(numero))
    
def factorial(x):
    for i in range(1,x):
        x = x*i    
    return x

x = int(input("ingrese un numero: "))
print("el factorial de",x,"es",factorial(x))


 
'''  
opcion = input("desea agregar algun numero a la lista(y o n): ")

while opcion == "y":
    agregarALista()
    opcion = input("desea agregar algun numero a la lista(y o n): ")

print(lista)
'''
    
#prom = calculoPromedio(3, 5)
#print(prom)