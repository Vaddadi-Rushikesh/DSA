class Car:

    #class variable, that reflects to all the objects
    wheels= 3

    #for declaring variable in a class, sused for attribute for instanced objects. This is instance variable
    def __init__(self,brand,color):
        self.brand= brand
        self.color= color

    #methods initialization for behaviour ob the object
    def info(self):
        print("this car is ",self.brand," with color ",self.color,"having wheels ",self.wheels)

    #comapre function
    def compare(self,other):
        if (self.color==other.color):
            return True
        else:
            return False

car1= Car("bmw", "black")
car2 = Car("porsche","black")

#updating the class variable using the class name
Car.wheels = 4

car1.info()
car2.info()

# if(car1.compare(car2)):
#     print("they are same")
# else:
#     print("they are different")
