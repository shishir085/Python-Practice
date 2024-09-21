class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.__model=model
    
    @property
    def model(self):
        return self.__model
    
        

    def fname(self):
        return f"{self.brand}{self.__model}"
    
mycar=Car("tata","safari")
# mycar.model="city"

Car("tata","nexon")

print(mycar.model)




