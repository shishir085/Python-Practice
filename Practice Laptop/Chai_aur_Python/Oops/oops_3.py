class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def fname(self):
        return f"{self.brand}{self.model}"
    
mycar=Car("tata","safari")
mynewcar=Car("toyota","suv")

class Electric_car(Car):
    def __init__(self, brand, model,battery_size):
            self.battery_size=battery_size
            super().__init__(brand, model)

    # def fname(self):
    #      return super().fname()

mytesla=Electric_car("tesla"," model s","85kWh")
print(mytesla.fname())
