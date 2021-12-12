'''
OOP
Class : blueprint
Objects : instances

Classes have attribute / properties
Classes can have behaviors - they can do things (called 'methods')

'''
# define classes with capital letters
# 'self' is a variable within a class that allows you to store values in class
# '__init__' - is a special method that initalizes. It is short for initialize
# classes allows you to store state of a variable

class Car:
  def __init__(self, num_wheels, num_seats, engine_size, fuel):
    self.num_wheels = num_wheels
    self.num_seats = num_seats
    self.engine_size = engine_size
    self.fuel = fuel
    self.on = False # car initally off
  
  def refuel(self, added_fuel):
    self.fuel += added_fuel

  def start(self):
    self.on = True
  
  def stop(self):
    self.on = False


if name == "__main__":
  car = Car(4, 5, 2, 50)  # using the class to make an object / instance.
  print(car.num_wheels)
  car.num_wheels = 6
  print(car.num_wheels)

  print(car.fuel)
  car.refuel(10)
  print(car.fuel)

  print(car.on)
  car.start()
  print(car.on)
  car.stop()
  print(car.on)