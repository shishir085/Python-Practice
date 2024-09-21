class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def fname(self):
        return f"{self.brand} {self.model}"

mycar=Car("toyota","corolla")
mynewcar=Car("tata","saffari")

print(mycar.model)
print(mycar.brand)
print(mycar.fname())