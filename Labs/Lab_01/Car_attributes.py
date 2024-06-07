class Car():
    print("\nCar\'s information: ")

    def __init__(self):
        self.Car_maker = ""
        self.Purchase_year = 0
        self.Purchase_price = 0.0

    def print_Car_maker(self):
        print(f"\tCar maker is: {self.Car_maker}")

    def print_Purchase_year(self):
        print(f"\tPurchase year is: {self.Purchase_year}")

    def print_Purchase_price(self):
        print(f"\tPurchase price is: ${self.Purchase_price:.2f}\n")

Car1 = Car()
Car1.Car_maker = input()
Car1.print_Car_maker()
Car1.Purchase_year = int(input())
Car1.print_Purchase_year()
Car1.Purchase_price = float(input())
Car1.print_Purchase_price()