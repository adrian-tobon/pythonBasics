class prueba():
    variable1 = None
    variable2 = None
    __variable4 = None

    def __init__(self, v1,v2):
        self.variable1 = v1
        self.variable2 = v2
        self.variable3 = "Adrian"
    
    
    def __printAtributos(self):
        print(self.variable1,self.variable2)
        
        
    def imprimir(self):
        self.__printAtributos()    
        
    def printAtributosDiccionario(self, **diccionario):
        for clave,valor in diccionario.items():
            print("clave:{",clave,"} - valor:{",valor,"}")
    
    @property    
    def variable4(self):
        return self.__variable4 
    
            
    @variable4.setter      
    def variable4(self,value):
        self.__variable4 = value
    
           



              

test = prueba("hola","mundo");
test.variable5 = "tobon"
print(test.variable3)
print(test.variable5)

test.imprimir();        
test.printAtributosDiccionario(nombre="juan",apellido="lopez") 

test.variable4 = 300  
print(test.variable4)   
    