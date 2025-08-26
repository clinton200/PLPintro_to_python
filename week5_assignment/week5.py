# question 1

class smartphone:
    def __init__(self, brand, model, battery_life, storage_space,year_of_man):
        self._brand = brand
        self._model = model
        self._battery_life = battery_life
        self._storage = storage_space
        self._year = year_of_man

    def check_storage(self):
        return self._storage
    
phone1 = smartphone("onePlus","onePlus9", 24, "64gb", 2021)
print(phone1._brand)
print(phone1._model)
print(phone1._battery_life)
print(phone1._storage)
print(phone1._year)


# Add an inheritance layer to explore polymorphism or encapsulation.
class BadBankAcount:
    def __init__(self,balance):
        self.balance = balance

account = BadBankAcount(0.0)
account.balance = -1

print(account.balance)

# encapsulation
class BankAccount:
    def __init__(self):
        self._balance =0.0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError ("withdrawal amount must be positive")
        if amount >= self._balance:
            raise ValueError("Insufficient balance")
        self._balance -= amount

account1 = BankAccount()
print(account1.balance)

#account1.balance = -1

account1.deposit(1.99)
print(account1.balance)
account1.withdraw(1)
print(account1.balance)
account1.withdraw(100)


# Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, 
# while Plane.move() prints "Flying" ✈️)

# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")

# Car class
class Car(Vehicle):
    def move(self):
        return "Driving"

# Plane class
class Plane(Vehicle):
    def move(self):
        return "Flying"

# Boat class
class Boat(Vehicle):
    def move(self):
        return "Sailing"

# Bike class
class Bike(Vehicle):
    def move(self):
        return "Riding"

# Demonstrating polymorphism
vehicles = [Car(), Plane(), Boat(), Bike()]

for v in vehicles:
    print(f"{v.__class__.__name__}: {v.move()}")
