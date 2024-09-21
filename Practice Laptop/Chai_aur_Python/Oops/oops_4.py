#  encapsulation

#   __ to make a private variable

class Car():
    def __init__(self,brand ,model):
        self.__brand=brand
        self.model=model

    def get_brand(self):
        return self.__brand+" !"



mycar=Car("tata","safari")

# print(mycar.__brand  )
print(mycar.get_brand())