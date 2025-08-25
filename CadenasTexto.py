'''
Created on 30/06/2025

@author: catobon
'''
cadena1 = "Monty \"temp\" Python"
print(cadena1)

print(cadena1[0:5])
print(cadena1[:3])
print(cadena1[5:])
print("------------------")

cadenaDividida = cadena1.split(" ")

print(cadenaDividida[0])
print(cadenaDividida[1])
print(cadenaDividida[2])

print("------------------")

cadena2 = "hola"
cadena3 = "Luis"


cadenaT = cadena2 + " " + cadena3

print(cadena2,cadena3,"prueba de concatenación multiple")

print(type(str(1)))

print("-------------------")

cadena3 = "ejemplo de prueba de substring"
print(cadena3)
print(len(cadena3))
print(cadena3[:-3])

print("-------------------")

cadenaPrueba = "Te quiero solo como amigo"
print(cadenaPrueba[0:2])
print(cadenaPrueba[-3:])
print(cadenaPrueba[::2])#coge toda la cadena, la recorre y cada dos posiciones imprimir
print(cadenaPrueba[::-1])
print(cadenaPrueba+cadenaPrueba[::-1])



