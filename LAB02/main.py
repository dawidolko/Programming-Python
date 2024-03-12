import math
import random

# 1. Wypróbuj kod z _listingów_ znajdujących się w instrukcji i sprawdź ich działanie.

print("Hello world!")
a = []
a.extend(range(2, 20))
print(a)
print(str(12))
print(list(range(10, 20, 3)))

def my_func():
    print("spam")
    print("spam")
    print("spam")

my_func()

# To wywołanie zostanie zakomentowane, ponieważ spowoduje błąd.
# hello()

def hello():
    print("hello")

def shout(word):
    """
    komentarz wieloliniowy
    """
    # komentarz jednoliniowy
    print(word + "!")


def print_with_exclamation(word):
    print(word + "!")


print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")


def print_sum_twice(x, y):
    print(x + y)
    print(x + y)


print_sum_twice(2, 5)


def function(var):
    var += 1
    print(var)


function(7)
# print(var) # To wywołanie zostanie zakomentowane, ponieważ spowoduje błąd.
def max(x, y):
    if x >= y:
        return x
    else:
        return y

print(max(4, 6))
z = max(9, 3)
print(z)

def add_numbers(x, y):
    sum = x + y
    return sum
    print("Ten napis nie wyświetli się")

print(add_numbers(4, 5))


shout("spam")

# 2. Napisz funkcję _lotto_, która do zwracanej listy wpisze 6 losowych i nie powtarzających się liczb z zakresu od 1 do 49.
def lotto():
    list = []
    while len(list) < 6:
        num = random.randrange(1, 49, 1)
        if not num in list:
            list.append(num)
    return list

print(lotto())

# 3. Stworzony na poprzednich zajęciach kalkulator edytuj tak aby wykorzystywał on funkcję do obliczania wybranych przez użytkownika działań (funkcje przyjmują po 2 parametry i zwracają wynik obliczeń).

def sum(first, second):
    return first + second


def subtraction(first, second):
    return first - second


def multiplication(first, second):
    return first * second


def division(first, second):
    return first / second


def exponentiation(first, second):
    return first ** second

# 4. Do kalkulatora dopisz możliwość obliczania pola/obwodu koła. (do wzoru wykorzystaj zaimportowaną wartość liczby Pi).

def length(radius):
    return 2 * math.pi * radius


def field(radius):
    return math.pi * pow(radius, 2)

# 5. Napisz funkcję, która sumuje liczby z listy podanej jako parametr i podaj ją (tą funkcję) jako parametr do innej funkcji, która odczyta liczby znajdujące się w pliku każda w nowej linii.

def sumList(list):
    sum = 0
    for x in list:
        sum += x
    return sum

def readFile(func):
    list = []
    with open("ex5.txt") as file:
        for line in file:
            list.append(int(line))

    return func(list)


print("Suma liczb w pliku: " + str(readFile(sumList)))

# 6. Do kalkulatora dopisz funkcję, która umożliwi użytkownikowi zapis działań oraz wyniku dla obliczenia pola/obwodu okręgu do pliku tekstowego.

def save(type, radius):
    with open("ex6.txt", "a") as file:
        if type == "length":
            file.write("Length (r=" + str(radius) + "): " + str(length(radius)) + "\n")

        if type == "field":
            file.write("Field (r=" + str(radius) + "): " + str(field(radius)) + "\n")


sign = input("""
Wybierz działanie:
    + dodawanie
    - odejmowanie
    * mnożenie
    / dzielenie
    ^ potęgowanie
    . obwód koła
    .. pole koła

Type here: """)

if sign == ".." or sign == ".":
    radius = float(input("Promien: "))
else:
    first = int(input("Pierwsza liczba: "))
    second = int(input("Druga liczba: "))

if sign == "+":
    print(sum(first, second))
elif sign == "-":
    print(subtraction(first, second))
elif sign == "*":
    print(multiplication(first, second))
elif sign == "/":
    print(division(first, second))
elif sign == "^":
    print(exponentiation(first, second))
elif sign == ".":
    print(length(radius))
    save("length", radius)
elif sign == "..":
    print(field(radius))
    save("field", radius)


# 7. Napisz funkcję wyznaczającą rozwiązania równania kwadratowego. Funkcja przyjmuje 3 parametry _a, b, c_ i rozwiązania zapisuje do pliku _result.txt_
def quadraticEquation(a, b, c):
    delta = pow(b, 2) - 4 * a * c

    if delta < 0:
        print("Ten trójmian nie ma miejsc zerowych.")
        with open("result.txt", "a") as file:
            file.write("w(x) = " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + "\n")
            file.write("Ten trójmian nie ma miejsc zerowych.\n\n")
    elif delta == 0:
        x = -b / (2 * a)
        print("Ten trójmian ma jedno miejsce zerowe w : x=" + str(x))
        with open("result.txt", "a") as file:
            file.write("w(x) = " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + "\n")
            file.write("Ten trójmian ma jedno miejsce zerowe w : x=" + str(x) + "\n\n")
    else:
        square = math.sqrt(delta)
        x1 = (-b + square) / (2 * a)
        x2 = (-b - square) / (2 * a)
        print("Ten trójmian ma miejsca zerowe w: x1=" + str(x1) + " oraz x2=" + str(x2))
        with open("result.txt", "a") as file:
            file.write("w(x) = " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + "\n")
            file.write("Ten trójmian ma miejsca zerowe w: x1=" + str(x1) + " oraz x2=" + str(x2) + "\n\n")


quadraticEquation(1, 0, 1)
