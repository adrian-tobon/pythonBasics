verdadero = True
falso = False

print(type(verdadero))
print(type(falso))

print(int(verdadero))
print(int(falso))


num1 = 500
num2 = 400

print(num1 < num2)
print(num1 > num2)


print(num1 < num2 or type(num1) == int)
print(num1 > num2 and not type(num1) == str)


c1 = "Comparacion de String"
c2 = "Comparation of String"

print(c1 != c2)

print(c1.startswith("Comp"))