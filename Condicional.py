'''
num1 = 500
num2 = 500

if num1 > num2 :
    print("num1 es mayor que num2")
elif num1 < num2:
    print("num2 es mayor que num1")
else:
    print("ambos numeros son iguales") 
    
'''   
'''    
vocales = "aeiouAEIOU"

letra = input("ingrese una letra: ")


if letra in vocales:
    print("Es vocal")
else:
    print("No es vocal")       
    
'''
'''
numero =int(input("Pro favor ingrese un numero entero: "))

if numero >= 0:
    print("Su valor absoluto es", numero)
else:
    print("Su valor absoluto es", numero*-1)    
'''
'''
a, b = map(str,input("ingrese dos palabra separadas por espacio: ").split(" "))

if a[-3:] == b[-3:]:
    print("las palabras riman")
elif a[-2:] == b[-2:]:            
    print("las palabras riman un poco")
else:
    print("las palabras no riman")    
'''

voto = input("Ingrese el candidato por el que quiere votar: ")

voto = voto.upper()

if voto == "A":
    print("Usted ha votado por el partido Rojo")
elif voto == "B":
    print("Usted ha votado por el partido Verde")
elif voto == "C":
    print("Usted ha votado por el partido Azul")
else:    
    print("El opcion ingresada es erronea")
        

    