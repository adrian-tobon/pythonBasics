'''
lista = [1, "perro",3.56,True,3,5,67,5,23,5,91,"casa",5]
tupla = ("Juan",300,5.678,False)
diccionario = {"uno":1,"dos":2,"tres":3}
dicc2 = {1:"uno", 2:"dos",3:"tres"}

print(type(lista))
print(type(tupla))
print(type(diccionario))

lista.append(300)
lista.insert(3, False)
print(lista.count(5))
print(lista.index(3.56))


lista2 = [1,3,2.4,3.7,0.3]
print(lista2)
lista2.sort()
print(lista2)

print(lista)



sublista = lista[-1]
print(sublista)
'''
'''
lista = [20, 50, "Curso", 'Python', 3.14]
print(lista)
a,b = map(str,input("ingrese los datos a cambiar:  ").split(" "))

lista[0] = a
lista[1] = b

print(lista)
'''
'''
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)

lista[4] = lista[4]*2
lista[7] = lista[7]*2
lista[9] = lista[9]*2
print(lista) 
'''
'''

diccionario = {"uno":1,"dos":2,"tres":3}
print(diccionario.get("cuatro","Vacio"))
print(diccionario.keys())
print(diccionario.values())
diccionario["dos"] = 2.0
diccionario["cuatro"] = 4

print(diccionario)
diccionario.pop("cinco",print("No existe esta llave"))
diccionario.setdefault("cinco", 5)
print(diccionario)
diccionario.update({"cinco":5.0})

diccionario2= diccionario.copy()
print(diccionario2)
print(type(diccionario))
'''
'''
paisesCapitales = {"Guatemala": "Ciudad de Guatemala",
                    "El Salvador": "San Salvador", "Honduras": "Honduras",
                    "Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama",
                    "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", 
                    "España": "Madrid"}

pais = input("por favor ingrese el nombre del pais: ")

pais = pais.capitalize()

print("Capital: " + paisesCapitales.get(pais, "No hay registro"))
'''
'''
jugadores = {

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}


numero = int(input("por favor ingrese el numero: "))
print("Nombre del jugador: " + jugadores.get(numero, "No hay registros de jugador para ese numero"))
'''
'''
conjunto1 = {1,2,3,4,5}
conjunto2 = set([5,6,7,8,9])
conjunto3 = set((10,11,12,13,14))
print(type(conjunto1))
print(type(conjunto2))
print(conjunto3)

conjunto2.add(20)
print(conjunto2)


conjunto2.update(conjunto1)
conjuntoTemp = conjunto2.difference(conjunto1)
conjuntoTemp2 = conjunto2.union(conjunto1)
conjuntoTemp3 = conjunto2.intersection(conjunto1)

print(conjunto2)
print(conjuntoTemp)
print(conjuntoTemp2)
print(conjuntoTemp3)


tupla = ("Juan",300,5.678,False)
print(tupla.count(5.678))
print(tupla.index(5.678))
'''
'''
mesesAnio = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
             "Agosto","Septiembre","Octubre","Noviembre","Diciembre")

numeroMes = int(input("por favor ingresar el numero del mes: "))

print("el mes es: " + mesesAnio[numeroMes-1])
'''

alfabeto = ("a","b","c","d","e","f","g","h","i",
            "j","k","l","m","n","o","p","q","r",
            "s","t","u","v","w","x","y","z")

numeroLetra = int(input("ingrese el numero de la letra: "))

print("la letra es: " + alfabeto[numeroLetra - 1])



















