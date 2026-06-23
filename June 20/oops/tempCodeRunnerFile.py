class Human:
    def __init__(self,name,age):
        self.name = name 
        self.__age = age

    def __str__(self):
        return f"Sab kuch maje mein {self.name}. Your age is {self.__age}"
    
    
class Female(Human):
    def __init__(self,name,age):
        # Human.__init__(self,name,age)
        super(name,age)
        gender = 'F'


obj1 = Human("hasib",15)
obj2 = Human("Ujjwal",16)
ob3 = Female("Anjali",17)

print(ob3) #output => -1
