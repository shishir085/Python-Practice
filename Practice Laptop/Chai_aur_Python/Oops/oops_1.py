#  basic class and object


class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

mycar=Car("toyota","corolla")

print(mycar.brand,":",mycar.model)

mynewcar=Car("tata","safari")

print(mynewcar.brand,":",mynewcar.model)





# class Bike:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

# mybike=Bike("honda","splender")

# print(mybike.brand,":",mybike.model)
