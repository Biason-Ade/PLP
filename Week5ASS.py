# ASSIGNEMENT 1
class Savings:
    def __init__(self, amount, weeks):
        self.amount = amount
        self.weeks = weeks

    def total_saving(self):
        return self.amount * self.weeks

save_year = Savings(100, 52)
total_savings = save_year.total_saving()
print(total_savings)
#ACTIVITY
class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing 🚢")

class Bird:
    def move(self):
        print("Flying in the sky 🦅")

class Fish:
    def move(self):
        print("Swimming in water 🐟")

# List of different objects
things = [Car(), Plane(), Boat(), Bird(), Fish()]

# Calling move() on each object
for thing in things:
    thing.move()
