#Ex.2, 3, 4
class Osoba:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Student(Osoba):
    def __init__(self, name, surname, albumNumber):
        super().__init__(name, surname)
        self.albumNumber = albumNumber

    def __str__(self):
        return "Czesc! Jestem " + self.name + " " + self.surname + " a moj numer albumu to " + str(self.albumNumber) + "."

s1 = Student("Dawid", "Olko", 122344)
s2 = Student("Mokebe", "Nzinga", 123432)
s3 = Student("Agatha", "Cristie", 133321)

print(s1)
print(s2)
print(s3)

#Ex. 5
class Number:
    def __init__(self, number):
        self.number = number;

    def __add__(self, other):
        return pow(self.number, 2) + 2*self.number*other.number + other.number

n1 = Number(2)
n2 = Number(2)
print("\nSuma dwoch klas Number: " + str(n1+n2))

#Ex.6
class Dog:
    count = 0
    dogs = []

    def __init__(self, name):
        self.name = name  # self.name is an instance variable
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self, n):  # this is an instance method
        print("{} says: {}".format(self.name, "woof! " * n))

    def show(self):
        print("Psow w liscie: " + str(self.count))
        for val in self.dogs:
            print(val, " ")


d1 = Dog("Fafik")
d2 = Dog("Azor")
d3 = Dog("Fafel")
print()
d2.show()
d3.show()
print()

#Ex. 7
class Pizza:
    _pineapple_allowed = False

    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        self._pineapple_allowed = value


pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)
