'''
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
print("Hola {} tienes {} años".format(nombre,edad))
'''
'''
a , b , c = map(int,input("por favor ingrese los valores de a, b y c: ").split())
print(a)
print(b)
print(c)

resultadoMas = (-b + ((b ** 2 - (4*a*c)) ** (1/2))) / (2*a)
resultadoMenos = (-b - ((b ** 2 - (4*a*c)) ** (1/2))) / (2*a)
print("el resultado es: x1=" + str(resultadoMas) + " x2=" + str(resultadoMenos))


p1 , p2 , p3 = map(float,input("por favor ingrese las notas de las tres practicas: ").split())

ep = float(input("ingrese la nota del examen parcial: "))

ef = float(input("ingrese la nota del examen final: "))

pp = (p1 + p2 + p3)/3

prom = (pp + 2*ep + 3*ef)/6


print("Promedio final: " + str(prom))
'''
'''
vocal, letter = map(str, input("por favor ingrese una vocal en minuscula y una letra en mayuscula").split())

vocal = vocal.upper()
letter = letter.lower()

print(vocal+letter)
'''
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
sexo = input("Ingresa tu sexo: ")


print("Te llamas: {}\nTu edad es: {}\nEres: {}".format(nombre,edad,sexo))


