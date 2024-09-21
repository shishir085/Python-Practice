# static

# it makes funciton that can be only accessed by class name not by object
#   use @staticmethod to  make static funciton
class Car():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    

mycar=Car("tata","safari")

# print(mycar.general_description())
print(Car.general_description())