class padre():
    variable1 = None
    variable2 = None
    __variable3 = None
    
    def __init__(self, variable1, variable2):
        self.variable1 = variable1
        self.variable2 = variable2   
        
    @property    
    def variable3(self):
        return self.__variable3
    
    @variable3.setter    
    def variable3(self, value):
        self.__variable3 = value 
    
class hija1(padre):
    
    variable4 = None
    
    def __init__(self,variable1,variable2,variable4):
        super().__init__(variable1,variable2)
        self.variable4 = variable4        
        
    def __str__(self):
        return str(self.variable1) + " " + str(self.variable2) + " " + str(self.variable3)          


obj1 = hija1("valor 2",67,3.33)
obj1.variable3 = 500
print(obj1.variable3) 



obj2 = hija1("valor 1", 400,800)
obj2.variable3 = 4.56
print(obj2.__str__())
   