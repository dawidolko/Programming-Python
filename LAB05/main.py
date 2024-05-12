# 1. Wypróbuj kod z listingów znajdujących się w instrukcji i sprawdź ich działanie.
print("\n\nZADANIE ", "1.","\n\n")

class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs


felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

print(felix.color)

class Dog:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()


class Dog:
    legs = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color


fido = Dog("Fido", "brown")
print(fido.legs)
print(Dog.legs)

class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
        print("Woof")

husky = Dog("Max", "grey")
husky.bark()

class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

# 3. Napisz klasę Osoba która będzie posiadać atrybuty takie jak imię i nazwisko.
# Edytuj klasę Student by dziedziczyła po klasie osoba i dodatkowo posiadała atrybut numer_albumu.
# Utwórz 3 różne obiekty tej klasy a następnie wypisz informacje o nich.
print("\n\nZADANIE ", "3.","\n\n")

class Osoba:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

# 2. Napisz prostą klasę Student która będzie posiadać atrybuty takie jak imię i numer albumu. Utwórz 3 różne obiekty tej klasy.
print("\n\nZADANIE ", "2.","\n\n")

class Student(Osoba):
    def __init__(self, name, surname, albumNumber):
        super().__init__(name, surname)
        self.albumNumber = albumNumber

    def __str__(self):
        return "Czesc! Jestem " + self.name + " " + self.surname + " a moj numer albumu to " + str(self.albumNumber) + "."

# 4. Do klasy Student dopisz metodę po której wywołaniu student się przedstawi. Cześć nazywam się imię nazwisko i mój numer albumu to nr_albumu
print("\n\nZADANIE ", "4.","\n\n")

s1 = Student("Dawid", "Olko", 125148)
s2 = Student("Piotr", "Smoła", 333222)
s3 = Student("Kimmy", "Riconen", 132322)

print(s1)
print(s2)
print(s3)

# 5. Napisz klasę Liczba mającą jeden atrybut przechowujący liczbę i nadpisz wybraną z magicznych metod tak aby realizowała działanie
print("\n\nZADANIE ", "5.","\n\n")
class Number:
    def __init__(self, number):
        self.number = number;

    def __add__(self, other):
        return pow(self.number, 2) + 2*self.number*other.number + other.number

n1 = Number(2)
n2 = Number(2)
print("\nSuma dwoch klas Number: " + str(n1+n2))

# 6. Do poniższej klasy dopisz metodę statyczną która wypisze liczbę obiektów (piesków) znajdujących się w liście i wypisze imiona wszystkich obiektów.
# Przetestuj kod na co najmniej dwóch obiektach.
print("\n\nZADANIE ", "6.","\n\n")
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

# 7. Napisz metodę która ustawi właściwość pineapple_allowed na wartość odpowiednią wartośćktóra będzie podana jako parametr do tej metody.
# Zadanie dotyczy fragmentu kodu z opisu właściwości. (Dla chętnych)
print("\n\nZADANIE ", "7.","\n\n")
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