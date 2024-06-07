
class Vehicle:
    print("\nCar\'s information: \n")

    def __init__(self):
        self.name = ""
        self.max_speed = 0
        self.mileage = 0.0
    
    def print_manufacturer(self):
        print("\nThe Car manufacturer, make, and model is: {}".format(self.name))
    
    def print_max_speed(self):
        print("\nThe Car max speed is {} mph".format(self.max_speed))

    def print_mileage(self):
        print("\nThe Car mileage is {}\n".format(self.mileage))

Bus = Vehicle()
Bus.name = input("\nEnter Car Manufacturer: ")
Bus.max_speed = float(input("Enter Car max speed in mph: "))
Bus.mileage = input("Enter Car mileage in city mpg/ highway mpg: ")
Bus.print_manufacturer()
Bus.print_max_speed()
Bus.print_mileage()