#encapsulation
class Car:
    def __init__(self, speed, color):
        #private attributes
        self.__speed = speed
        self.__color = color

    def set_speed(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

car1 = Car(500, "white")
#print(car1.__speed) = error
car1.set_speed(1000)
print(car1.get_speed())



#myClass creation with private variables
class myClass():
        __privateVar = 27

        def __privMet(self):
            print('This is a private method')

        def hello(self):
            print("The private variable is: ", myClass.__privateVar)

t1 = myClass()
#t1.__privateVar = attribute error
t1.hello()



#class Computer with setter
class Computer():
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()
c.setMaxPrice(1000)
c.sell()



#class Point with coordinate points
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

p1 = Point(2,3)
print(p1)