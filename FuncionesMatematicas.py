import math 
import random

print(pow(2, 8))
print(math.sqrt(64))
print(math.factorial(6))
print(random.randint(1,100))

'''
def getSin(x):
    return math.sin(x)

def getCos(x):
    return math.cos(x)

def getTan(x):
    return math.tan(x)


x = int(input("ingrese el numero: "))
print("El seno de",x,"es igual a",getSin(x))
print("El coseno de",x,"es igual a",getCos(x))
print("La tangente de",x,"es igual a",getTan(x))
'''
'''
x,y = map(int, input("Ingrese dos numeros: ").split(" "))

def mayorOMenor(x,y):
    if x > y :
        return 1
    elif y > x:
        return-1
    else:
        return 0
    
print(mayorOMenor(x, y))
'''
'''
def total():
    
    monto = int(input("ingrese el monto: "))
    iva = int(input("ingrese el porcentaje de IVA: "))
    
    
    if iva != 0 :        
        if iva >= 0:
            return monto + (monto*(iva/100))        
        else:
            return "El valor del iva debe ser mayor o igual que cero"     
    else:
        return monto + (monto*(21/100))
    
    
print(total())    
'''     

def areaRectangulo(base,altura):
    return base * altura

def areaCirculo(radio):
    return math.pi*(math.pow(radio, 2))
        
print(areaRectangulo(3, 5))
print(areaCirculo(3))



