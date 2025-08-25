from mailbox import NoSuchMailboxError


class Estudiante():
    _nombre = None
    _nota = None
    
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota
        
    @property    
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,value):
        self._nombre = value
        
        
    @property    
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self,value):
        self._nota = value
        
    def getNombre(self):
        print(self._nombre)    
        
    def getNota(self):
        print(self._nota)
        
        
    def Aprobado(self):
        if self._nota >= 3.0 :
            print("El estudiante",self._nombre,"ha aprobado")
        else:
            print("El estudiante",self._nombre,"no ha aprobado")
            
'''            
est1 = Estudiante("Jorge",3.4)
est2 = Estudiante("Luis",2.4)            
        
est1.Aprobado()
est2.Aprobado()        
'''        

class Calculadora():
    def __init__(self):
     self.a, self.b = map(int,input("por favor ingrese dos numeros, deprados por espacio: ").split(" "))
        
    def suma(self):
        print(str(self.a + self.b))
        
    def resta(self):
        print(str(self.a - self.b))
        
    def multiplicacion(self):
       print(str(self.a * self.b))
        
    def division(self):
       print(str(self.a / self.b))
 
'''        
calc = Calculadora()
calc.suma()
calc.resta() 
calc.multiplicacion() 
calc.division()             
'''
class Fabrica():
    def __init__(self, llantas,color,precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
        

class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

    @property
    def llantas(self):
        return self._llantas
    
    @property
    def color(self):
        return self._color
    
    @property
    def precio(self):
        return self._precio
    
    
class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)

    @property
    def llantas(self):
        return self._llantas
    
    @property
    def color(self):
        return self._color
    
    @property
    def precio(self):
        return self._precio

'''
beewings = Moto(2,"azul",12000000)
pathfinder = Carro(4,"verde",80000000)

print("El vehiculo beewings tiene",beewings.llantas," llantas, es de color",beewings.color,"y su precio es de",beewings.precio,"millones")
print("El vehiculo pathfinder tiene",pathfinder.llantas," llantas, es de color",pathfinder.color,"y su precio es de",pathfinder.precio,"millones")
'''

class Marino():
    def hablar(self):
        print("Hola....")
        
        
class Pulpo(Marino):
    def hablar(self):
        super().hablar()
        print("Soy un pulpo")
        
        
class Foca(Marino):
    def hablar(self, mensaje):
        self.mensaje = mensaje
        super().hablar()
        print(mensaje)        
''' 
marino = Marino()
marino.hablar() 
       
pulpo = Pulpo()
pulpo.hablar()        
    
foca = Foca()
foca.hablar("Soy una foca")    
''' 

class Universidad():
    def __init__(self, universidad):
        self.nombre_universidad = universidad

class Carrera():
    def __init__(self, carrera):
       self.carrera = carrera

class Estudiante(Universidad,Carrera):
    def __init__(self, universidad, carrera, nombre,edad):
        Universidad.__init__(self,universidad)
        Carrera.__init__(self,carrera)
        self.nombre = nombre
        self.edad = edad
        
obj1 = Estudiante("EAFIT","ingenieria de Sistemas","Luis", 38)
print(obj1.nombre_universidad,obj1.carrera,obj1.nombre,obj1.edad)

        

      