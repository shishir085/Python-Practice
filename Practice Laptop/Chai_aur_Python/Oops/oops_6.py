# polymorphism

class Car:
    totalcar=0

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.totalcar+=1

        
    def fname(self):
        return f"{self.brand}{self.model}"
    
    def fuel_type(self):
         return "petrol or desiel"
    
mycar=Car("tata","safari")
mynewcar=Car("toyota","suv")
test=Car("test","test")

class Electric_car(Car):
    def __init__(self, brand, model,battery_size):
            self.battery_size=battery_size
            super().__init__(brand, model)

    def fuel_type(self):
        return "Electric charge"

    # def fname(self):
    #      return super().fname()

mytesla=Electric_car("tesla"," model s","85kWh")
print(mytesla.fuel_type())
safari=Car("tata","safari")
safari3=Car("tata","nexon")

# print(safari.fuel_type())

print(Car.totalcar)