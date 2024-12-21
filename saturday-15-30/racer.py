import math
import random
def mult(x, y):
    return x * y

def abc():
    print("abc")

def

#x = 0
#while x < 10:
#    print(x)
#    x+=1

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#for x in numbers:
#    print(x)


#for x in range(2,10):
#    print(x)

class Car:
    def __init__(self, name, max_speed, fuel_type, fuel_amount, engine):
        self.name = name
        self.speed = max_speed
        self.fuel_type = fuel_type
        self.fuel_amount = fuel_amount
        self.engine = engine
    def __str__(self):
        return f"Car({self.speed}, {self.fuel_type}, {self.fuel_amount}, {self.engine})"

class Racer:

    def __init__(self, name, age, streak, car):
        self.name = name
        self.age = age
        self.streak = streak
        self.car = car

    def __str__(self):
        return f"Racer({self.name}, {self.age}, {self.streak}, {self.car})"

class Race:
    def __init__(self, length):
        self.length = length
        self.winners = []
    def doRace(self, racer1, racer2):
        winner = random.choice([racer1, racer2])
        return winner


toyota = Car("Toyota", 200, "бензин", 100, None)
ziguli = Car("Жигули", 1000000, "самогон", 200, "magic")
zina = Racer("Баба Зина", math.inf, 0, ziguli)
kristian = Racer("Kritsian", 13, 0, toyota)

print(racer)

# Увеличить streak у победителя
# Заправить машину
# Вывести на экран всех победителей
